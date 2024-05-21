#!/usr/bin/env python3.11 
# from manager.manager import Manager
# from renderer.terminal import Terminal
from networking.server import JSONSocketServer
import socket

if __name__ == "__main__":
    
    HOST = socket.gethostname()  # Change this to your desired host
    PORT = 5000        # Change this to your desired port

    server = JSONSocketServer(HOST, PORT)
    server.start()    
    # term.run()

