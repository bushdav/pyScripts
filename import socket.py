import socket

srv_addr=raw_input("enter IP :") #172.16.170.129
srv_prt=int(input("enter port nbr:"))

my_sock= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
my_sock.bind((srv_addr,srv_prt))
my_sock.listen(4)
clientconnection,address=my_sock.coonect((srv_addr,srv_prt))
print(" server connected",address)

msg= input("Message to send:")
my_sock.sendall(msg.encode())
my_sock.close()