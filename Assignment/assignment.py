import sys
import socket
import os

# CLIENT SENDS
# INPUT: cli_sock,"sunglasses.png"
def send_file(socket, filename):
    
	# ASSUMING file is in directory, open it
	# ASIDE "rb" stands for "read in byte mode"
	print("Opening file in read bytes mode")
	file = open(filename,"rb")
	print("Getting the file_size from the os")
	file_size = os.path.getsize(filename)
	
	print("Whoosh!!! sending filename and size")
	socket.send(filename.encode())
	socket.send(str(file_size).encode())
	
	print("Reading the data...")
	data = file.read()

	print("Sending all through the socket!!!")
	socket.sendall(data)
	# b stands for bytes, so sending bytes of end to signify end of send
	socket.send(b"<END>")
	print("Closing the file...")
	file.close()
	print("File sent successfully!!!")

# SERVER RECIEVES
# cli_sock, "sunglasses.png"  
def recv_file(socket, filename):
	print("Server!!!")
	print("The recv_file has been called!!!")
	
	print("Creating the file to start writing to!")
	file = open(filename,"wb")

	print("Starting data transfer!!!")
	file_bytes = b""
	done = False
	while not done:
		data = socket.recv(1024)
		if file_bytes[-5:] == b"<END>":
			done = True
		else:
			file_bytes += data
	
	file.write(file_bytes)
	file.close()
      
def send_listing(socket):
      print("hello")
      
def recv_listing(socket):
      print("hello")