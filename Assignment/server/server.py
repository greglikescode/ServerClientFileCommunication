import sys
import socket

from assignment import send_file, recv_file, send_listing, recv_listing

# Create the socket on which the server will receive new connections
srv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Try to bind the server to name "0.0.0.0" and its address is set by user input, which will be 1069
# python server.py 1069

try:
	srv_sock.bind(("0.0.0.0", int(sys.argv[1]))) # sys.argv[1] is the 1st argument on the command line
	srv_sock.listen()
	
except Exception as e:
	# Print the exception message
	print(e)
	# Exit with a non-zero value, to indicate an error condition
	exit(1)

# Loop forever (or at least for as long as no fatal errors occur)
while True:
	try:
		print("Waiting for new client... ")
		
		cli_sock, cli_addr = srv_sock.accept()
		
        # Translating to string to be used in user output
		cli_addr_str = str(cli_addr)

		print("Client " + cli_addr_str + " connected.")

		command = cli_sock.recv(1024)
		file_name = cli_sock.recv(1024)
		print("HELLO THE COMMAND IN SERVER IS"+str(command))
		
	except Exception as e:
		# Print the exception message
		print(e)
	    # Exit with a non-zero value, to indicate an error condition
		exit(1)

	while True:
		try:
			
			recv_file(cli_sock,file_name)
		
		finally:
			
			cli_sock.close()

# Close the server socket as well to release its resources back to the OS
srv_sock.close()

# Exit with a zero value, to indicate success
exit(0)