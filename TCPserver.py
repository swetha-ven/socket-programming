from socket import *
import math
 
def compute():
    sum = 0
    for num in list:
        sum += int(num)
        mean = sum/length
    print('Sum of the numbers: ', sum)
    print('Highest number: ', max(list))
    print('Lowest number: ', min(list))
    print('Mean of the numbers: ', round(mean,2))
    
TCP_IP = '127.0.0.1'
TCP_PORT = 12000
serverSocket = socket(AF_INET,SOCK_STREAM) #Create a TCP/IP socket
serverSocket.bind((TCP_IP,TCP_PORT))    #Bind the TCP/IP socket to the TCP port
serverSocket.listen(1)  #Looking for connections
print('The server is ready to receive.')
while True:
    connectionSocket, addr = serverSocket.accept()  #Accepts connection from the client
    data = connectionSocket.recv(20).decode() #Receive data from the client - lower response time
    if not result: break
    print ('Received data from the client successfully! Data: ', data)
    result = list.compute()
    connectionSocket.send(result.encode())
    connectionSocket.close()
