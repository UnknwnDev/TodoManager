#!/usr/bin/env python3.11 
from manager.manager import Manager
# from renderer.terminal import Terminal


if __name__ == "__main__":
    manager = Manager()
    # term = Terminal()
    
    manager.run(True)
    
    # term.run()