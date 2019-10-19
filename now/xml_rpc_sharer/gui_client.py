from xmlrpclib import ServerProxy, Fault
from node_server import Node, UNHANDLED
from controller import randomString
from threading import Thread
from time import sleep
from os import listdir
import sys
import wx

HEAD_START = 0.1 # Seconds
SECRET_LENGTH = 100


class Client(wx.App):
    """
    The main client class, which takes care of setting up
    the GUI and starts a Node for serving files.
    """
    def __init__(self, url, dirname, urlfile):
        """
        Creates a random secret, instantiates a Node with
        that secret, starts a Thread with the Node's _start
        method (making sure the Thread is a deamon so it
        will quit when the application quits), reads all the
        URLs from the URL file and introduces the Node to them.
        """
        super(Client, self).__init__()
