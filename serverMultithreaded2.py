from socket import *
import time
import threading

serverPort = 3000

serverSocket = socket(AF_INET, SOCK_STREAM)

# Prepare a sever socket
serverSocket.bind(('', serverPort))
serverSocket.listen(0)


def start_thread(connectionSocket, addr):
    time.sleep(5)
    print(addr)
    try:
        message = connectionSocket.recv(1024).decode()
        print(message)

        filename = message.split()[1]
        f = open(filename[1:])

        output_data = f.read()
        connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode())

        connectionSocket.sendall(output_data.encode())
        connectionSocket.sendall("\r\n".encode())

        connectionSocket.close()
    except IOError:
        connectionSocket.sendall("HTTP/1.1 404 Not Found\r\n\r\n".encode())
        connectionSocket.close()


while True:
    # Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    threading.Thread(target=start_thread, args=(connectionSocket, addr,)).start()

serverSocket.close()
sys.exit()  # Terminate the program after sending the corresponding data
