import sys
import socket

from ae1 import *  # ae1 holds all of our functions

srv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host_name = "0.0.0.0"

try: # this initialises our server
    srv_sock.bind((host_name, int(sys.argv[1])))
    srv_sock.listen()
except Exception as e:
    print("Error:", e)
    exit(1)

while True: # keep running listening for connections forever (until we close the program)
    try:
        report = ""
        cli_sock, cli_addr = srv_sock.accept()
        cli_addr_str = str(cli_addr)
        report = "Client: " + cli_addr_str + ", "

        data_received = cli_sock.recv(2048).decode()  # Increase the buffer size if needed
        
        if "\n" in data_received:
            file_name, cmd = data_received.split("\n")
        else:
            cmd = data_received.strip()
            file_name = None

        report += "Filename: "+file_name+", Command: "+cmd+", "
        print (report,end="")
        if cmd == "put" and file_name:
            try:
                recv_file(cli_sock, file_name)
            except Exception as e:
                print("Error receiving file:", e)
        elif cmd == "get" and file_name:
            try:
                send_file(cli_sock, file_name)
            except Exception as e:
                print("Error sending file:", e)
        elif cmd == "list":
            try:
                send_listing(cli_sock)
            except Exception as e:
                print("Error sending file list:", e)
        else:
            print("Invalid command:", cmd)
        cli_sock.close()  # Close the client socket after processing one request

    except Exception as e:
        print("Error:", e)
        break  # Exit the loop on any exception

srv_sock.close()  # Close the server socket
