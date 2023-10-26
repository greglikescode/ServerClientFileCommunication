import sys
import socket
import os

# UPLOAD
def send_file(socket, filename):
	try:
		#Opening file in read bytes mode and reading data within it
		file = open(filename,"rb")
		data = file.read()

		# Sending all data through socket + an END signifier, then closing
		socket.sendall(data) # NOTE no need to encode since already in bytes
		socket.send(b"<END>")
		file.close()
	except Exception as e:
		pass

# DOWNLOAD
def recv_file(socket, filename):
	try:
		file = open(filename,"wb")
		file_bytes = b""
		done = False
		while not done:
			data = socket.recv(1024)
			if file_bytes[-5:] == b"<END>": # Write the data until reach <END>
				done = True
			else:
				file_bytes += data
		file.write(file_bytes)
		file.close()
	except Exception as e:
		pass
      
def send_listing(socket):
	library = os.listdir() # library is a type list
	try:
		# Sending library as a bunch of strings
		lib_string = ""
		for elt in library:
			lib_string = lib_string + elt + "\n"
		# Chopping of \n character at end of lib_string
		lib_string = lib_string[:-1]
		socket.send(lib_string.encode())
	except Exception as e:
		pass
      
def recv_listing(socket):
	try:
		data_recieved = socket.recv(1024).decode()
		library = data_recieved.split("\n")

		# Printing one file per line to the screen
		for elt in library:
			print(elt)
	except Exception as e:
		pass