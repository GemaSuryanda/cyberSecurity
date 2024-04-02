import socket

conection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection.connect(("192.168.1.10", 4444))
