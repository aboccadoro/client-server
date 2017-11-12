from socket import *
import re

'''
Variables representing the server name and arbitrary,
valid port number.
'''
serverName = '127.0.0.1'
serverPort = 55000
'''
Step 2. Open a TCP socket to the server
'''
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

message = ""

while (message != "quit"):
	#Step 1. read in input from the user by keyboard and print to console
	message = input("\nEnter a valid mathematical expression or \"quit\" to exit: ")
	print ("\n")
	print ("-->> Client request: '" + message + "'")
	#Step 3. Send the request to the server
	clientSocket.sendto(message.encode(), (serverName, serverPort))
	#Step 4. Receive the status code and result
	modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
	query = re.search('\[.+\]', modifiedMessage.decode())
	status = query.group(0)
	#Step 5. status code is 200 OK
	if (status == "[200 OK]"):
		print ("<<-- Server response: '" + modifiedMessage.decode() + "'")
	#Step 5. status code is 300
	elif (status == "[300]"):
		print ("<<-- Server response: '" + modifiedMessage.decode() + "' -Warning: invalid operation.")

print ("\n ++++   Client Program Ends   ++++\n")
clientSocket.close()