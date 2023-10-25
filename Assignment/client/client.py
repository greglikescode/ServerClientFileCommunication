import sys
import socket

sys.path.append("..")
from assignment import send_file, recv_file, send_listing, recv_listing

# Commands
commands = ["put","get","list","exit"]
# Create the socket with which we will connect to the server
# It will be an internet socket that will be a TCP socket
cli_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# The server's address is a tuple, comprising the server's IP address or hostname, and port number
# so for our example, the first arguement will be "local host" and the second will be 1069, which looks like
#   0       [0]       [1]     [2] [3]     [4]
# python client.py localhost 1069 put sunglasses.png 
srv_addr = (sys.argv[1], int(sys.argv[2]))

# Convert to string, to be used shortly, used to print out the servers address
srv_addr_str = str(srv_addr)

# ESTABLISHING THE CONNECTION
try:
	print("Connecting to " + srv_addr_str + "... ")
	cli_sock.connect(srv_addr)
	print("Connected.")
except Exception as e:
	print(e)
	exit(1)

try:
	command = str(sys.argv[3])
	filename = str(sys.argv[4])

	if command not in commands:
		print("Error, command not in list of commands")
		exit(1)

	# Sending the filename and command to server...
	cli_sock.send(command.encode())

	if command == "put":
		print("CLIENT IS GOING TO ATTEMPT TO SEND "+filename+" THROUGH THE SOCKET "+str(cli_sock))
		send_file(cli_sock,filename)
	elif command == "get":
		while file_received != True:
			print("Waiting for server to send the file")
	elif command == "list":
		print("Some more stuff will go here")
	elif command == "exit":
		print("Somehow exit the code")
		

finally:
	cli_sock.close()

# Exit with a zero value, to indicate success
exit(0)
