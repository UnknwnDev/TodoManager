import socket
import json
import threading
from manager.manager import Manager

class JSONSocketServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.manager = Manager()

    def handle_client(self, client_socket, address):
        print(f"Accepted connection from {address}")
        try:
            while True:
                data = client_socket.recv(1024).decode()
                if not data:
                    break

                try:
                    received_data = json.loads(data)
                except json.JSONDecodeError:
                    print("Error decoding JSON data from client")
                    continue  # Skip processing this data

                if 'command' in received_data:
                    command = received_data['command']
                    if command == 'list_tasks':
                        result = self.manager.get_all_tasks()
                    elif command == 'remove_task':
                        result = self.manager.remove_task(received_data.get('id', ''))
                    elif command == 'save_task':
                        result = self.manager.save_task(received_data.get('category', ''))
                    # Add more commands here as needed

                    return_str = json.dumps(result, default=lambda o: o.__dict__,
                                            sort_keys=True, indent=2)
                    client_socket.send(return_str.encode())
                    client_socket.close()

        except ConnectionResetError:
            print(f"Connection reset by {address}")
        
        except OSError as e:
            print(f"Error with client socket: {e}")

        finally:
            # client_socket.close()
            print(f"Closed connection from {address}")

            

    def start(self):
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        print("Server is listening for connections...")
        try:
            while True:
                client_socket, address = self.server_socket.accept()
                client_thread = threading.Thread(target=self.handle_client, args=(client_socket, address))
                client_thread.start()
        except KeyboardInterrupt:
            print("Server closed due to keyboard interrupt.")
            self.server_socket.close()

# Example usage:
if __name__ == "__main__":
    server = JSONSocketServer('127.0.0.1', 8080)
    server.start()
