from socket import *
import time
import re

'''
Variables representing the server name and arbitrary,
valid port number.
'''
serverName = input("\nServer name: ")
serverPort = 60000

'''
Opening a UDP socket.
'''
clientSocket = socket(AF_INET, SOCK_DGRAM)

message = ""
while (message != "quit"):
	#Step 1. read in input from the user by keyboard and print to console
	message = input("\nEnter a valid mathematical expression or \"quit\" to exit: ")
	print ("\n")
	print ("-->> Client request: '" + message + "'")
	#Step 2. send the input request to the server
	clientSocket.sendto(message.encode(), (serverName, serverPort))
	clientSocket.setblocking(0)
	#Step 3. begin waiting from d = 0.1s for a response
	d = 0.1
	while (d < 2.0):
		try:
			#Step 5. a reply is received 
			clientSocket.settimeout(d)
			modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
			modifiedMessage = modifiedMessage.decode()
			query = re.search('\[.+\]', modifiedMessage)
			status = query.group(0)
			#Step 6. status code is 200 OK
			if (status == "[200 OK]"):
				print ("<<-- Server response: '" + modifiedMessage + "'")
			#Step 7. status code is 300
			elif (status == "[300]"):
				print ("<<-- Server response: '" + modifiedMessage + "' -Warning: invalid operation.")
			clientSocket.settimeout(None)
			break
		except timeout:
			#Step 4. the timeout expires and is either incremented or the client halts
			d = 2 * d
			if (d > 2.0):
				raise
			print ("\n")
			print ("-->> Client request: '" + message + "'")
			clientSocket.sendto(message.encode(), (serverName, serverPort))

print ("\n ++++   Client Program Ends   ++++\n")
clientSocket.close()