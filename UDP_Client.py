from socket import *
import time

serverName = "127.0.0.1"
serverPort = 60000

clientSocket = socket(AF_INET, SOCK_DGRAM)

message = ""
while (message != "quit"):
	message = input("\nEnter a valid mathematical expression or \"quit\" to exit: ")
	print ("\n")
	print ("-->> At client request to send out: '" + message + "'")
	clientSocket.sendto(message.encode(), (serverName, serverPort))
	clientSocket.setblocking(0)
	d = 0.1
	while (d < 2.0):
		try:
			clientSocket.settimeout(d)
			modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
			print ("<<-- At Client response received: '" + modifiedMessage.decode() + "'")
			clientSocket.settimeout(None)
			break
		except timeout:
			d = 2 * d
			if (d > 2.0):
				raise
			print ("\n")
			print ("-->> At client request to send out: '" + message + "'")
			clientSocket.sendto(message.encode(), (serverName, serverPort))

print ("\n ++++   Client Program Ends   ++++\n")
clientSocket.close()