from socket import *
 
TCP_IP = '127.0.0.1'
TCP_PORT = 12000
clientSocket = socket(AF_INET, SOCK_STREAM) #Create a TCP/IP socket
clientSocket.connect((TCP_IP, TCP_PORT))    #Connect the TCP/IP socket to the TCP port
input_num = input('Input numbers separated by space: ') #Get the integers
list = input_num.split()    #Separate each integer with a whitespace
print('Data sent: ', list)
clientSocket.send(list.encode())    #Send the data to the server
size = input('Input length of numbers: ')   #Get the length of integers
length = int(size)  #Size is of type int now
print('Data sent: ', length)
clientSocket.send(length.encode())    #Send the data to the server
data = clientSocket.recv(1024)  #Receive the computed results from the server
print('From Server\n', data.decode())
clientSocket.close()    #clear connection
