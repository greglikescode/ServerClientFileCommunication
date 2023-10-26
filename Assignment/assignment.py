import sys
import socket
import os

# CLIENT SENDS
# INPUT: cli_sock,"sunglasses.png"
def send_file(socket, filename):
	try:
		print("Opening file in read bytes mode")
		file = open(filename,"rb")
		# print("Getting the file_size from the os")
		# file_size = os.path.getsize(filename)
		
		# print("Whoosh!!! sending file size")
		# socket.sendall(str(file_size).encode())
		
		print("Reading the data...")
		data = file.read()

		print("Sending all through the socket!!!")
		socket.sendall(data)
		socket.send(b"<END>") # b stands for bytes, so sending bytes of end to signify end of send
		print("Closing the file...")
		file.close()
		print("File sent successfully!!!")

	except Exception as e:
		print("Error sending file",e)
		exit(1)

# SERVER RECIEVES
# cli_sock, "sunglasses.png"  
def recv_file(socket, filename):
	print("The recv_file has been called!!!")

	# file_size = socket.recv(1024).decode()
	print("filename: "+filename)
	# print("file size: "+file_size)
	
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
	
	print("Data transfer complete! closing file...")
	file.write(file_bytes)
	file.close()
      
def send_listing(socket):
	print("hello, I am send_listing() !!!!")
	library = os.listdir() # library is a type list
	print("This is the library: "+str(library))
	try:
		# Sending library as a bunch of strings
		lib_string = ""
		for elt in library:
			lib_string = lib_string + elt + "\n"
		# Chopping of \n character at end of lib_string
		lib_string = lib_string[:-1]
		print("Sending this: "+lib_string)
		socket.send(lib_string.encode())
		print("Finished sending!!!")
	except Exception as e:
		print("Library could not send",e)
      
def recv_listing(socket):
	print("hello, I am recv_listing() !!!")

	try:
		data_recieved = socket.recv(1024).decode()
		data_recieved.split("\n")
		print("Library recieved: \n"+data_recieved)
	except Exception as e:
		print("Library recieve failure",e)