import sys
import socket

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

# Loop forever (or at least for as long as no fatal errors occur)
while True:
	# ESTABLISHING THE CONNECTION
	try:
		print("Waiting for new client... ")
		cli_sock, cli_addr = srv_sock.accept()
		cli_addr_str = str(cli_addr)
		print("Client " + cli_addr_str + " connected.")
	except Exception as e:
		print(e)
		exit(1)

	while True:
		try:
			#command = cli_sock.recv(1024).decode()
			
			#if command == "put":
				#recv_file(cli_sock,filename)
			filename = cli_sock.recv(1024).decode()
			print(filename)
			file_size = cli_sock.recv(1024).decode()
			print(file_size)
			
			file = open(filename,"wb")

			file_bytes = b""
			done = False
			while not done:
				data = cli_sock.recv(1024)
				if file_bytes[-5:] == b"<END>":
					done = True
				else:
					file_bytes += data
				
			file.write(file_bytes)
			file.close()
		
		finally:
			
			cli_sock.close()

# Close the server socket as well to release its resources back to the OS
srv_sock.close()

# Exit with a zero value, to indicate success
exit(0)