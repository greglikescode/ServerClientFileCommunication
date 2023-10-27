import sys
import os
import socket

sys.path.append("..")
from assignment import send_file, recv_file, recv_listing

cli_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#           [0]       [1]     [2] [3]     [4]
# python client.py localhost 1069 put sunglasses.png 
srv_addr = (sys.argv[1], int(sys.argv[2]))
srv_addr_str = str(srv_addr)
port_str = str(int(sys.argv[2]))

# Commands
commands = ["put","get","list","exit"]

try:
	command = str(sys.argv[3])
except Exception as e:
	print(srv_addr_str,port_str,"FAILURE REPORT: you must input a command after port number.",e," Exitting code...")
	exit(1)

if command not in commands:
	print(srv_addr_str,port_str,"FAILURE REPORT:",command,"is an invalid command.",e," Exitting code...")
	exit(1)

try:
	filename = str(sys.argv[4])
except Exception as e:
	pass # No filename is necessary for list and exit

# ESTABLISHING THE CONNECTION
try:
	print("Connecting to " + srv_addr_str + "... ")
	cli_sock.connect(srv_addr)
	print("IP address:",srv_addr_str,"port number:",port_str,"client now connected to server")

	try:
		datasend = f"{command}\n{filename}"
		cli_sock.sendall(datasend.encode())
	# If no filename was input...
	except:
		cli_sock.sendall(command.encode())	
	
except Exception as e:
	print(srv_addr_str,port_str,"FAILURE REPORT: could not connect to server at",srv_addr_str,port_str,". Exitting code...")
	exit(1)

try:
	current_directory = os.listdir()
	# CLIENT UPLOAD
	if command == "put":
		if filename in current_directory:
			try:
				if send_file(cli_sock,filename):
					print(srv_addr_str,port_str,"SUCCESS REPORT: "+filename+" was successfully sent to the server.")
				else:
					print(srv_addr_str,port_str,"FAILURE REPORT: failed to send "+filename+".")
			except Exception as e:
				print(srv_addr_str,port_str,"FAILURE REPORT: failed to send "+filename+".",e)
		else:
			print(srv_addr_str,port_str,"FAILURE REPORT: "+filename+" could not be found in client directory")
				

	# CLIENT DOWNLOAD
	elif command == "get":

		if filename not in current_directory:
			try:
				if recv_file(cli_sock,filename):
					print(srv_addr_str,port_str,"SUCCESS REPORT: "+filename+" was successfully downloaded from the server.")
				else:
					print(srv_addr_str,port_str,"FAILURE REPORT: failed to recieve "+filename+".")
			except Exception as e:
				print(srv_addr_str,port_str,"FAILURE REPORT: failed to recieve "+filename+".",e)
		else:
			print(srv_addr_str,port_str,"FAILURE REPORT: overwriting is not permitted.")
			exit(1)

	# LIST
	elif command == "list":
		recv_listing(cli_sock)
		print(srv_addr_str,port_str,"SUCCESS REPORT: server directory was recieved.")

	# EXIT
	elif command == "exit":
		print(srv_addr_str,port_str,"SUCCESS REPORT: exitting code...")
		exit(0)	

finally:
	cli_sock.close()

# Exit with a zero value, to indicate success
exit(0)
