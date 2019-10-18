from asyncore import dispatcher
from asynchat import async_chat
import socket, asyncore

PORT = 5005
NAME = 'ICQ'


class EndSession(Exception): pass


class CommandHandler:
    """
    Simple command handler similar to cmd.Cmd from
    the standard library.
    """
    def unknown(self, session, cmd):
        """Respond to an unknown command"""
        session.push(("Unknown command: %s\r\n" % cmd).encode('utf-8'))

    def handle(self, session, line):
        """Handle a received line from a given session"""
        if not line.strip(): return
        # split off the command:
        parts = line.split(' ', 1)
        cmd = parts[0]
        try:
            line = parts[1].strip()
        except IndexError:
            line = ''
        # Find a handler
        method = getattr(self, 'do_' + cmd, None)
        # if it is callable...
        if callable(method):
            # ...call it:
            method(session, line)
        else:
            # Otherwise, respond to the unknown command:
            self.unknown(session, cmd)


class Room(CommandHandler):
    """
    A generic environment that may contain one or more
    users (sessions).It takes care of basic command
    handling and broadcasting.
    """
    def __init__(self, server):
        self.server = server
        self.sessions = []

    def add(self, session):
        """A session (user) has entered the room"""
        self.sessions.append(session)

    def remove(self, session):
        """A session (user) has left the room"""
        self.sessions.remove(session)

    def broadcast(self, line):
        """Send a line to all sessions in the room"""
        for session in self.sessions:
            session.push(line.encode('utf-8'))

    def do_logout(self, session, line):
        """Respond to the logout command"""
        raise EndSession


class LoginRoom(Room):
    """
    A room meant for a single person who has just connected.
    """

    def add(self, session):
        Room.add(self, session)
        # When a user enters, greet him/her
        self.broadcast('Welcome to %s\r\n' % self.server.name)

    def unknown(self, session, cmd):
        # All unknown commands (anything except login
        # or logout) results in a prodding:
        session.push(('Please log in\nUse "login <nick>"\r\n').encode())

    def do_login(self, session, line):
        name = line.strip()
        # Make sure the user has entered a name:
        if not name:
            session.push('Please enter a name\r\n'.encode())
        # Make sure that the name isn't in use:
        elif name in self.server.users:
            session.push(('The name "%s" is taken.\r\n' % name).encode())
            session.push('Please try again.\r\n'.encode())
        else:
            # The name is OK, so it is stored in the session, and
            # the user is moved into the main room.
            session.name = name
            session.enter(self.server.main_room)


class ChatRoom(Room):
    """
    A room meant for multiple users who can chat with
    the others in the room.
    """
    def unknown(self, session, line):
        self.do_say(session, line)

    def add(self, session):
        # Notify everyone that a new user has entered:
        self.broadcast(session.name + ' has entered the room.\r\n')
        self.server.users[session.name] = session
        Room.add(self, session)

    def remove(self, session):
        Room.remove(self, session)
        # Notify everyonbe that a user has left:
        self.broadcast(session.name + ' has left the room.\r\n')

    def do_say(self, session, line):
        self.broadcast(session.name + ': ' + line + '\r\n')

    def do_look(self, session, line):
        ###Handles the look command, used to see who is in a room###
        session.push('The following are in this room:\r\n'.encode())
        for other in self.sessions:
            session.push((other.name + '\r\n').encode())

    def do_who(self, session, line):
        ###Handles the who command, used to see who is logged in###
        session.push('The following are logged in:\r\n'.encode())
        for name in self.server.users:
            session.push((name + '\r\n').encode())


class LogoutRoom(Room):
    """
    A simple room for a single user. Its sole purpose
    is to remove the user's name from the server.
    """
    def add(self, session):
        # When a session (user) enters the LogoutRoom it is deleted
        try:
            del self.server.users[session.name]
        except KeyError:
            pass


class ChatSession(async_chat):
    """
    A class that takes care of a connection between
    the server and a single user.
    """
    def __init__(self, server, sock):
        # Standard setup tasks:
        async_chat.__init__(self, sock)
        self.server = server
        self.set_terminator(b"\r\n")
        self.data = []
        self.name = None
        # All sessions begin in a separate LoginRoom:
        self.enter(LoginRoom(server))
        # Greet the user:
        #self.push((">>> Welcome to %s<<<\r\n" % self.server.name).encode('utf-8'))

    def enter(self, room):
        # Remove self from current room and add self to
        # next room...
        try:
            cur= self.room
        except AttributeError:
            pass
        else: cur.remove(self)
        self.room = room
        room.add(self)

    def collect_incoming_data(self, data):
        self.data.append(data)

    def found_terminator(self):
        """
        If a terminator is found, that means that a full
        line has been read. Broadcast it to everyone.
        """
        line = ''
        try:
            line = ''.join([x.decode() for x in self.data])
        except Exception:
            pass
        self.data = []
        try:
            self.room.handle(self, line)
        except EndSession:
            self.handle_close()
        # process line
        #self.server.broadcast(self, line)

    def handle_close(self):
        async_chat.handle_close(self)
        self.enter(LogoutRoom(self.server))


class ChatServer(dispatcher):
    """
    A class that receives connections and spawns individual
    sessions. It also handles broadcasts to these sessions.
    """
    def __init__(self, port, name):
        # Standard setup tasks
        dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind(('', port))
        self.listen(5)
        self.name = name
        self.users = {}
        self.main_room = ChatRoom(self)

    def handle_accept(self):
        conn, addr = self.accept()
        ChatSession(self, conn)


if __name__ == '__main__':
    s = ChatServer(PORT, NAME)
    try:
        asyncore.loop()
    except KeyboardInterrupt:
        print()
