import sys
import os
import socket

sys.path.append("..")
from assignment import send_file, recv_file, send_listing

srv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#   0      [0]      [1]
# python server.py 1069
try:
	srv_sock.bind(("0.0.0.0", int(sys.argv[1]))) # sys.argv[1] is the 1st argument on the command line
	srv_sock.listen(5)	
except Exception as e:
	print("FAILURE REPORT: could not perform srv_sock.bind() and srv_sock.listen().",e,"Exitting code...")
	exit(1)

i = 0
# Loop forever until error.
while True:
	print("TRANSFER",i)
	# ESTABLISHING THE CONNECTION
	try:
		print("Waiting for new client to connect... ")
		cli_sock, cli_addr = srv_sock.accept()
		cli_addr_str = str(cli_addr)
		cli_port_str = str(int(sys.argv[1]))
		print("IP address:",cli_addr_str,"port number:",cli_port_str,"server up and running")

		# May need to increase buffer size!!!
		data_recieved = cli_sock.recv(1024).decode()
		try:
			command, filename = data_recieved.split("\n")
		except:
			command = data_recieved

		current_directory = os.listdir()

		# SERVER DOWNLOAD
		if command == "put":

			if filename not in current_directory:
				try:
					recv_file(cli_sock,filename)
					print(cli_addr_str,cli_port_str,"SUCCESS REPORT: "+filename+" was successfully downloaded from the client.")
				except Exception as e:
					print(cli_addr_str,cli_port_str,"FAILURE REPORT: could not recieve",filename+".",e)
			else:
				print(cli_addr_str,cli_port_str,"FAILURE REPORT: overwriting is not permitted.")

		# SERVER UPLOAD
		elif command == "get":

			if filename in current_directory:
				try:
					send_file(cli_sock,filename)
					print(cli_addr_str,cli_port_str,"SUCCESS REPORT: "+filename+" was successfully sent to the client.")
				except Exception as e:
					print(cli_addr_str,cli_port_str,"FAILURE REPORT: could not send file "+filename+" to the client.",e,"Exitting code...")
			else:
				print(cli_addr_str,cli_port_str,"FAILURE REPORT: "+filename+" could not be found in server directory")


		elif command == "list":
			send_listing(cli_sock)
			print(cli_addr_str,cli_port_str,"SUCCESS REPORT: server directory was sent")

		elif command == "exit":
			print(cli_addr_str,cli_port_str,"SUCCESS REPORT: exitting code...")
			srv_sock.close()
			exit(0)
		
	finally:
		cli_sock.close()
		i+=1