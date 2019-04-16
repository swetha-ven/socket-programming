# socket-programming
CMPE 148: Assignment #1

1.Write TCP client and server programs in Pythonthat the client gets a set ofintegers and the length of the set as command line arguments. Then the client sends the set to the server. Afterward, the server computes the total, the highest number, the lowest number, and the mean (in float) of the set and sendsthe results to the client. Finally, the client receives the results and prints them out. 

The TCP server program is run first so that the server can look for connections. When the server is ready to receive, it accepts the connection from the client. The server then receives data from the client at a lower response time since the buffer size is set to 20. The TCP client program is then run. On the client side, a TCP/IP socket is created and it is connected to the TCP port. A set of integers and their length are inputted. This data is then sent to the server. On the server side, the required data is computed using a function and the result is sent to the client. The connection is then closed. On the client side, the computed results are received from the server. The connection is then closed.

Test case:

The server is ready to receive. Input numbers separated by space: 2 4 7 -3 Data sent: 2 4 7 -3 Received data from the client successfully! Data: 2 4 7 -3 Input length of numbers: 4 Data sent: 4 Received data from the client successfully! Data: 4 From Server: Sum of the numbers: 10 Highest number: 7 Lowest number: -3 Mean of the numbers: 2.50

2.Repeat problem # 1 using UDP client and server programs.

The UDP server program is run first. A UDP/IP socket is created and it is connected to a UDP port. When the server is ready to receive, it starts receiving data from the client. The UDP client program is then run. On the client side, a UDP/IP socket is created. A set of integers and their length are inputted. This data is then sent to the server. On the server side, the required data is computed using a function and the result is sent to the client. The connection is then closed. On the client side, the computed results are received from the server. The connection is then closed.

Test case

The server is ready to receive. Input numbers separated by space: 5 7 -9 Data sent: 5 7 -9 Received data from the client successfully! Data: 5 7 -9 Input length of numbers: 3 Data sent: 3 Received data from the client successfully! Data: 3 From Server: Sum of the numbers: 3 Highest number: 5 Lowest number: -9 Mean of the numbers: 1.00
