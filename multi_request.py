import threading
from socket import *
import asyncio

server_host = 'localhost'
server_port = 3000
filename = "x.html"


# Define a function for the thread
def print_time(thread_name):
    print('{} Server start '.format(thread_name))
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((server_host, server_port))
    request = 'GET /{} HTTP/1.1\r\nHost: {}:{}\r\n\r\n'.format(filename, server_host, server_port)
    clientSocket.send(request.encode())

    res = ""
    while True:
        response = clientSocket.recv(1024)
        if str(response.decode()) == '':
            break
        res += str(response.decode())

    print(thread_name + '\n' + res + "*************************************")
    clientSocket.close()


# async def main():
#     await asyncio.gather(print_time('thread_1'), print_time('thread_2'), print_time('thread_3'))
# asyncio.run(main())
#  TODO: tai sao toi uncomment 3 dong ben tren thi bi loi

threading.Thread(target=print_time, args=("thread-1",)).start()
threading.Thread(target=print_time, args=("thread-2",)).start()
threading.Thread(target=print_time, args=("thread-3",)).start()
