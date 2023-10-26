import sys
import socket

sys.path.append("..")
from assignment import send_file, recv_file, send_listing, recv_listing

# Create the socket on which the server will receive new connections
srv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Try to bind the server to name "0.0.0.0" and its address is set by user input, which will be 1069
# python server.py 1069
try:
	srv_sock.bind(("0.0.0.0", int(sys.argv[1]))) # sys.argv[1] is the 1st argument on the command line
	srv_sock.listen(5)	
except Exception as e:
	print(e)
	exit(1)

i = 0
# Loop forever (or at least for as long as no fatal errors occur)
while True:
	print(i)
	# ESTABLISHING THE CONNECTION
	try:
		print("Waiting for new client... ")
		cli_sock, cli_addr = srv_sock.accept()
		cli_addr_str = str(cli_addr)
		print("Client " + cli_addr_str + " connected.")
		
		command = cli_sock.recv(1024).decode()
		filename = cli_sock.recv(1024).decode()
		file_size = cli_sock.recv(1024).decode()
		print("The file name is: "+filename)
		print("The file size is: "+file_size)
		print("The file command is: "+command)

		# SERVER DOWNLOAD
		if command == "put":
			print("Calling recv_file!!! Passing in filename")
			recv_file(cli_sock,filename)

		# SERVER UPLOAD
		elif command == "get":
			print("Calling send_file!!! Passing in filename")
			send_file(cli_sock,filename)
			serverSent = cli_sock.send(True.encode())


		elif command == "list":
			print("Some more stuff will go here")

		elif command == "exit":
			cli_sock.close()
			srv_sock.close()
			exit(0)

		else:
			print("Invalid command name")
		
	finally:
		print("I am in the finally")
			
		cli_sock.close()
		i+=1

# Close the server socket as well to release its resources back to the OS
srv_sock.close()

# Exit with a zero value, to indicate success
exit(0)