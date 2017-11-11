from socket import *
from Evaluator import *
import random

'''
Step 1. Step 2.
Specify an arbitrary, valid port number and create a socket
to bind the address information. Begin listening to the
socket.
'''
serverPort = 60000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))

'''
Strings to represent the response message to send back to
the client and the status code that was generated.
'''
modifiedMessage = ""
status = ""

print ("The UDP server is ready\n")
while (modifiedMessage != "Server is shutting down..."):
	#Step 3. Listening to the socket
	message, clientAddress = serverSocket.recvfrom(2048)
	#Step 4. Implementing UDP unreliability by accepting requests with probability .5
	if (random.random() > 0.49):
		print ("-->> At Server received message is: '" + message.decode() + "'")
		print (" -->> clientAddress is: ", str(clientAddress[0]) + "/" + str(clientAddress[1]))
		modifiedMessage = message.decode()
		if (modifiedMessage != "quit"):
			#Step 5. Parsing the request by spaces accepting the format 'x1 op x2'
			instr = modifiedMessage.split(" ")
			if (len(instr) == 3):
				x1 = instr[0]
				op = instr[1]
				x2 = instr[2]
				#Step 6. Checking the validity of the input
				if (is_number(x1) and is_number(x2)):
					result = evaluate(instr)
					#Step 8. Valid
					if (result != -1):
						status = "200 OK"
						modifiedMessage = str(result)
					#Step 7. Invalid: divide by zero
					else: 
						status = "300"
						modifiedMessage = "I can't compute that!"
				#Step 7. Invalid: incorrect number input
				else:
					status = "300"
					modifiedMessage = "I can't compute that!"
			#Step 7. Invalid: general incorrect input (specifically amount of words)
			else:
				status = "300"
				modifiedMessage = "I can't compute that!"
			print ("<<-- [" + status + "] At Server response to send back: '" + modifiedMessage + "'\n")
			serverSocket.sendto(modifiedMessage.encode(), clientAddress)
		#Step 8. Valid
		else:
			status = "200 OK"
			modifiedMessage = "Server is shutting down..."
			print ("<<-- [" + status + "] At Server response to send back: '" + modifiedMessage + "'\n")
			serverSocket.sendto(modifiedMessage.encode(), clientAddress)


print (" ++++   Server Program Ends   ++++\n")
serverSocket.close()