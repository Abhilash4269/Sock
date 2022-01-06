import socket

s = socket.socket() # by default it is tcp & ipv4

print('Socket Created')

s.bind(('localhost',9999))

s.listen(3)
print('waiting for connections')

while True:   # creating infinite loop
    c, addr = s.accept()
    name = c.recv(1024).decode()
    print('connected with', addr, name)
  
    c.send(bytes('Hello World!','utf-8'))
    
    c.close()