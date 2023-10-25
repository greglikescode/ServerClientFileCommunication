import sys
import socket

from assignment import send_file, recv_file, send_listing, recv_listing

commands = ["put","get","list"]

socket = sys.argv[2]
command = sys.argv[3]
file_name = sys.argv[4]

if command not in commands:
	print("Error, command not in list of commands")
	exit(1)
	


# Create the socket with which we will connect to the server
# It will be an internet socket that will be a TCP socket
cli_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# The server's address is a tuple, comprising the server's IP address or hostname, and port number
# so for our example, the first arguement will be "local host" and the second will be 1069, which looks like
# python client.py localhost 1069 "put"
srv_addr = (sys.argv[1], int(socket))

# Convert to string, to be used shortly, used to print out the servers address
srv_addr_str = str(srv_addr)

# Try to connect, if cannot connect...
try:
	print("Connecting to " + srv_addr_str + "... ")

	cli_sock.connect(srv_addr)
	
	print("Connected.")
	file_name = cli_sock.send(1024)
	command = cli_sock.send(1024)
	
except Exception as e:
	# Print the exception message
	print(e)
	# Exit with a non-zero value, to indicate an error condition
	exit(1)

try:

	if command == "put":
		send_file(cli_sock,sys.argv[4])
		
	elif command == "get":
		print("this is where stuff for get will go")
		
	elif command == "list":
		print("this is where stuff for get will go")
		

finally:
	cli_sock.close()

# Exit with a zero value, to indicate success
exit(0)
