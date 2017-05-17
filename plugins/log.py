#Socket client in python

import socket   #for sockets
import sys  #for exit

def log(msg):
	try: #handle exceptions
	    #create an AF_INET, STREAM socket (TCP)
	    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	except socket.error, msg:
	    print('Failed to create socket. Error code: ' + str(msg[0]) + ' , Error message : ' + msg[1])
	    sys.exit();
	print('Socket Created')
	#set host
	host = 'localhost'
	port = 8080
	try:
	    remote_ip = socket.gethostbyname( host )
	except socket.gaierror:
	    #could not resolve
	    print('Hostname could not be resolved. Exiting')
	    sys.exit()
	print('Ip address of ' + host + ' is ' + remote_ip)
	#connect to ip on a certain 'port' using the connect function.
	s.connect((remote_ip , port))
	print('Socket Connected to ' + host + ' on ip ' + remote_ip)
	try :
	    #Set the whole string
	    s.sendall(msg)
	except socket.error:
	    #Send failed
	    print('Sending failed')
	    sys.exit()
	print('Message send successfully')
	#Close the socket
	s.close()
