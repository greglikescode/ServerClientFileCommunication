import sys
import socket
import os

def send_file(socket, filename):
    # "rb" stands for "read in byte mode"
	file = open(filename,"rb")
	file_size = os.path.getsize(filename)
	
	socket.send(filename.encode())
	socket.send(str(file_size).encode())
	
	data = file.read()
	socket.sendall(data)
	# b stands for bytes, so sending bytes of end to signify end of send
	socket.send(b"<END>")
	file.close()
    
def recv_file(socket, filename):
	# print("in")
	filename = socket.recv(1024).decode()
	print("Filename:"+filename)
	file_size = socket.recv(1024).decode()
	print("File size:"+file_size)
	
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