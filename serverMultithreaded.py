from _thread import *
from socket import *
import time

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(10)


def multi_threaded_client(connection):
    try:
        # while True:  # While true de server luon phai xu ly client, dung de test xem co xu ly nhieu client duoc khong
        time.sleep(5)
        message = connection.recv(1024).decode()
        filename = message.split()[1]
        f = open(filename[1:])
        outputData = f.read()
        connection.send("HTTP/1.1 200 OK\r\n\r\n".encode())
        for i in range(0, len(outputData)):
            connection.send(outputData[i].encode())
        connection.send("\r\n".encode())
        connection.close()
    except IOError:
        connection.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())
        connection.close()


while True:
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    start_new_thread(multi_threaded_client, (connectionSocket,))

serverSocket.close()
sys.exit()
