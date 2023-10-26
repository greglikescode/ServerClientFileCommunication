import sys
import socket

sys.path.append("..")
from assignment import send_file, recv_file, send_listing, recv_listing

srv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
	srv_sock.bind(("0.0.0.0", int(sys.argv[1]))) # sys.argv[1] is the 1st argument on the command line
	srv_sock.listen(5)	
except Exception as e:
	print(e)
	exit(1)

i = 0
# Loop forever until error.
while True:
	print(i)
	# ESTABLISHING THE CONNECTION
	try:
		print("Waiting for new client... ")
		cli_sock, cli_addr = srv_sock.accept()
		cli_addr_str = str(cli_addr)
		print("Client " + cli_addr_str + " connected.")

		# May need to increase buffer size!!!
		data_recieved = cli_sock.recv(1024).decode()
		try:
			command, filename = data_recieved.split("\n")
			print("Command: "+command+"\nFilename: "+filename)
		except:
			command = data_recieved

		# SERVER DOWNLOAD
		if command == "put":
			try:
				print("Calling recv_file!!! Passing in "+filename)
				recv_file(cli_sock,filename)
			except Exception as e:
				print("Error recieving file",e)

		# SERVER UPLOAD
		elif command == "get":
			try:
				print("Calling send_file!!! Passing in"+filename)
				send_file(cli_sock,filename)
			except Exception as e:
				print("Error recieving file",e)


		elif command == "list":
			print("Some more stuff will go here")
			send_listing(cli_sock)

		elif command == "exit":
			print("Exitting code...")
			cli_sock.close()
			srv_sock.close()
			exit(0)

		else:
			print("Invalid command name. Please try aagin.")
		
	finally:
		print("I have reached finally")
		cli_sock.close()
		i+=1

# Close the server socket as well to release its resources back to the OS
srv_sock.close()

# Exit with a zero value, to indicate success
exit(0)