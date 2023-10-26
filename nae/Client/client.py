import sys
import socket

from ae1 import *

commands = ["put", "get", "list"]

command = sys.argv[3]
file_name = sys.argv[4]

if command not in commands:
    print("Error, command not in list of commands")
    exit(1)

cli_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
srv_addr = (sys.argv[1], int(sys.argv[2]))

try:
    print("Connecting to " + str(srv_addr) + "...")
    cli_sock.connect(srv_addr)
    print("Connected.")

    data_to_send = f"{file_name}\n{command}"
    cli_sock.sendall(data_to_send.encode())

except Exception as e:
    print("Error:", e)
    exit(1)

try:
    if command == "put":
        send_file(cli_sock, file_name)
    elif command == "get":
        recv_file(cli_sock,file_name)
    elif command == "list":
        print("this is where stuff for list will go")
finally:
    cli_sock.close()

exit(0)
