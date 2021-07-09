import http.client

srv_addr=raw_input('input the IP of the target: ')
srv_prt=input("enter the port number")
#urli='/'
try:
    connection=http.client.HTTPConnection(srv_addr,srv_prt)
    connection.request('OPTIONS','/')
    response=connection.getresponse()
    print("Server status : ", response.getheaders('allow'))
    connection.close()
except:
        print("CONNECTION FAILED")
