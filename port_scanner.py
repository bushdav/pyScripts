import socket
srv='172.16.170.129'
port='1,1000'    #str(input('enter port range: '))

lowport =int(port.split(',')[0])
highport=int(port.split(',')[1])

for prt in range(lowport,highport):
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    status=s.connect_ex((srv,prt))
    if status==0:
        print ("Port:",prt,"is open")
    else:
        print("Port: ",prt,"is closed")
