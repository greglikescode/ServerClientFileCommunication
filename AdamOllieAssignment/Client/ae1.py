import sys
import socket
import os

def send_file(socket, filename):
    try:
        # Open the file in binary mode
        with open(filename, "rb") as file:
            # Get file size
            file_size = os.path.getsize(filename)

            # Send file size first
            socket.sendall(str(file_size).encode())

            # Send file data in chunks
            chunk_size = 1024
            while True:
                data = file.read(chunk_size)
                if not data:
                    break
                socket.sendall(data)

            # Send the end marker
            socket.sendall(b"<END>")
            print("SUCCESS")
    except Exception as e:
        print("Error sending file:", e)

    
def recv_file(socket, filename):
    try:
        # Receive file size
        file_size = int(socket.recv(1024).decode())

        # Open the file in binary write mode
        with open(filename, "wb") as file:
            received_size = 0
            while received_size < file_size:
                # Receive data in chunks
                data = socket.recv(1024)
                file.write(data)
                received_size += len(data)
                # Check for the end marker
                if data[-5:] == b"<END>":
                    break

        print("SUCCESS")
    except Exception as e:
        print("Error receiving file:", e)

      
def send_listing(socket):
    try:
          file_list = os.listdir() # get list of files in current directory
          file_list_str = "\n".join(file_list)
          socket.sendall(file_list_str.encode())
          socket.sendall(b"<END>") # send end marker
          print ("SUCCESS")
    except Exception as e:
            print("Error sending file list: ",e)

      
def recv_listing(socket):
    try:
        file_list = ""
        while True:
            data = socket.recv(1024).decode()
            if data[-5:] == "<END>":
                file_list += data[:-5]
                break
            file_list += data
        print ("Received file list from server \n"+file_list)
    except Exception as e:
        print("Error receving file list:",e)