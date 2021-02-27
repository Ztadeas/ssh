import socket

ip = "192.168.1.43"
port = 22
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((ip, port))
while True:
    s.listen(0)
    print("Listening....")
    cleint, addr = s.accept()


  
