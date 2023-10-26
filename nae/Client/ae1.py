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
            print("File", filename, "successfully sent.")
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

        print("File", filename, "successfully received.")
    except Exception as e:
        print("Error receiving file:", e)

      
def send_listing(socket):
      print("hello")
      
def recv_listing(socket):
      print("hello")