from socket import *
UDP_IP = '127.0.0.1'
UDP_PORT = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM) #Create a UDP/IP socket
input_num = input('Input numbers separated by space: ') #Get the integers
list = input_num.split()    #Separate each integer with a whitespace
print('Data sent: ', list)
clientSocket.sendto(list.encode(),(UDP_IP, UDP_PORT))
size = input('Input length of numbers: ')   #Get the length of integers
length = int(size)  #Size is of type int now
print('Data sent: ', length)
clientSocket.sendto(length.encode(),(UDP_IP, UDP_PORT)) #Send the data to the server
data, serverAddress = clientSocket.recvfrom(2048)   #Receive the computed results from the server
print(data.decode()) clientSocket.close()   #clear connection
