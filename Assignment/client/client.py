import sys
import socket

sys.path.append("..")
from assignment import send_file, recv_file, send_listing, recv_listing

# Commands
commands = ["put","get","list","exit"]
try:
	command = str(sys.argv[3])
except Exception as e:
	print(e)
	print("No command was input. Exitting...")
	exit(1)

if command not in commands:
	print("Error, command not in list of commands")
	exit(1)

try:
	filename = str(sys.argv[4])
except Exception as e:
	print(e)
	print("No filename was input, continuing...")

cli_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#           [0]       [1]     [2] [3]     [4]
# python client.py localhost 1069 put sunglasses.png 
srv_addr = (sys.argv[1], int(sys.argv[2]))
srv_addr_str = str(srv_addr)

# ESTABLISHING THE CONNECTION
try:
	print("Connecting to " + srv_addr_str + "... ")
	cli_sock.connect(srv_addr)
	print("Connected.")

	# Sending the filename and command to server...

	# If no filename was input...
	try:
		datasend = f"{command}\n{filename}"
		cli_sock.sendall(datasend.encode())
	except:
		cli_sock.sendall(command.encode())	
	
except Exception as e:
	print(e)
	exit(1)

try:
	# CLIENT UPLOAD
	if command == "put":
		print("COMMAND ENTERED IS put")
		print("CLIENT IS GOING TO ATTEMPT TO SEND "+filename+" THROUGH THE SOCKET "+str(cli_sock))
		send_file(cli_sock,filename)

	# CLIENT DOWNLOAD
	elif command == "get":
		print("COMMAND ENTERED IS get")
		print("CLIENT IS GOING TO ATTEMPT TO RECIEVE "+filename+" THROUGH THE SOCKET "+str(cli_sock))
		recv_file(cli_sock,filename)

	# LIST
	elif command == "list":
		print("Some more stuff will go here")
		recv_listing(cli_sock)

	# EXIT
	elif command == "exit":
		print("Exitting...")
		exit(0)	

finally:
	cli_sock.close()

# Exit with a zero value, to indicate success
exit(0)
