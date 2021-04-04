import sys
from socket import *

clientSocket = socket(AF_INET, SOCK_STREAM)
params = sys.argv
clientSocket.connect((params[1], int(params[2])))
print(clientSocket.getsockname())
request = 'GET /{} HTTP/1.1\r\nHost:{}:{}\r\n\r\n'.format(params[3], params[1], params[2])
clientSocket.send(request.encode())
res = ""
while True:
    response = clientSocket.recv(1024)
    if str(response.decode()) == '':
        break
    res += str(response.decode())
print(res)
