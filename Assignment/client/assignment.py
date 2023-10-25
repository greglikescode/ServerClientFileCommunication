import sys
import socket
import os

# CLIENT SENDS
# INPUT: cli_sock,"sunglasses.png"
def send_file(socket, filename):
    
	# ASSUMING file is in directory, open it
	# ASIDE "rb" stands for "read in byte mode"
	file = open(filename,"rb")
	file_size = os.path.getsize(filename)
	
	socket.send("recieved_image.png".encode())
	socket.send(str(file_size).encode())
	
	data = file.read()
	socket.sendall(data)
	# b stands for bytes, so sending bytes of end to signify end of send
	socket.send(b"<END>")
	file.close()

# SERVER RECIEVES
# cli_sock, "sunglasses.png"  
def recv_file(socket, filename):
	filename = socket.recv(1024).decode()
	print(filename)
	file_size = socket.recv(1024).decode()
	print(file_size)
	
	file = open(filename,"wb")

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