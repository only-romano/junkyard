#! usr/bin/python
# Minimal threading server, Python 2.7
from SocketServer import TCPServer, ThreadingMixIn, StreamRequestHandler

class Server(ThreadingMixIn, TCPServer): pass

class Handler(StreamRequestHandler):

    def handle(self):
        addr = self.request.getpeername()
        print 'Got connection from', addr
        self.wfile.write("Thank you for threading connection!")

server = Server(('', 1235), Handler)
server.serve_forever()
