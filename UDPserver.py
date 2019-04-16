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
 
UDP_IP = '127.0.0.1'    
UDP_PORT = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)  #Create a UDP/IP socket
serverSocket.bind(('', serverPort)) #Bind the UDP/IP socket to the UDP port
print('The server is ready to receive')
while True:
    list, clientAddress = serverSocket.recvfrom(2048)   #Receive data from the client
    data = message.decode().compute()
    serverSocket.sendto(data.encode(), clientAddress)
