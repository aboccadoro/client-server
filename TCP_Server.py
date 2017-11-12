from socket import *
from Evaluator import *

'''
Step 1. Step 2.
Specify an arbitrary, valid port number and create a socket
to bind the address information. Begin listening to the
socket.
'''
serverPort = 55000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('127.0.0.1', serverPort))
serverSocket.listen(1)

'''
Strings to represent the response message to send back to
the client and the status code that was generated.
'''
modifiedMessage = ""
status = ""

conn, addr = serverSocket.accept()

print ("The TCP server is ready\n")
while (modifiedMessage != "[200 OK] Server is shutting down..."):
	#Step 3. Receive a request
	message = conn.recvfrom(2048)[0].decode()
	print ("-->> Client request: '" + message + "'")
	print (" -->> clientAddress is: ", str(addr[0]) + "/" + str(addr[1]))
	if (message != "quit"):
		#Step 4. Parsing the request by spaces accepting the format 'x1 oc x2'
		instr = message.split(" ")
		if (len(instr) == 3):
			x1 = instr[0]
			x2 = instr[2]
			#Step 6. Checking the validity of the input
			if (is_number(x1) and is_number(x2)):
				result = evaluate(instr)
				#Step 6. Valid
				if (result != -1):
					status = "200 OK"
					modifiedMessage = "[" + status + "] " + str(result)
				#Step 5. Invalid: divide by zero
				else:
					status = "300"
					modifiedMessage = "[" + status + "] " + str(result)
			#Step 5. Invalid: incorrect number input
			else:
				status = "300"
				modifiedMessage = "[" + status + "]"
		#Step 5. Invalid: general incorrect input (specifically amount of words)
		else:
			status = "300"
			modifiedMessage = "[" + status + "]"
		print ("<<-- Server response: '" + modifiedMessage + "'\n")
		conn.sendto(modifiedMessage.encode(), addr)
	#Step 6. Valid
	else:
		status = "200 OK"
		modifiedMessage = "[" + status + "] " + "Server is shutting down..."
		print ("<<-- [" + status + "] Server response: '" + modifiedMessage + "'\n")
		conn.sendto(modifiedMessage.encode(), addr)
		conn.close()


print (" ++++   Server Program Ends   ++++\n")
serverSocket.close()