import sys
import socket
from ae1 import *

srv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host_name = "0.0.0.0"

try:
    srv_sock.bind((host_name, int(sys.argv[1])))
    srv_sock.listen()
    print("Server listening on port", sys.argv[1])
except Exception as e:
    print("Error:", e)
    exit(1)

while True:
    try:
        print("Waiting for new client")
        cli_sock, cli_addr = srv_sock.accept()
        cli_addr_str = str(cli_addr)
        print("Client " + cli_addr_str + " connected.")

        data_received = cli_sock.recv(2048).decode()  # Increase the buffer size if needed
        file_name, cmd = data_received.split("\n")
        print("Filename:", file_name)
        print("Received command:", cmd)

        if cmd == "put":
            try:
                recv_file(cli_sock, file_name)
            except Exception as e:
                print("Error receiving file:", e)
        elif cmd == "get":
            
        else:
            print("Invalid command:", cmd)

        cli_sock.close()  # Close the client socket after processing one request

    except Exception as e:
        print("Error:", e)
        break  # Exit the loop on any exception

srv_sock.close()  # Close the server socket
