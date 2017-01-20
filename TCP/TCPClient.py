from socket import *
import urlparse

serverName = 'localhost'

serverPort = 12333

clientSocket = socket(AF_INET, SOCK_STREAM)

url = 'http://www.cs.utah.edu/~kobus/simple.html'

url = '/~kobus/simple.html'
url = urlparse.urlparse(url)


print(url.netloc)

# #Handshake in order to connect
# clientSocket.connect((serverName, serverPort))
#
# #Ask for message
# sentence = raw_input('Input lowercase sentence:')
#
# print sentence
#
# #Send message
# clientSocket.send(sentence.encode())
#
# #Receive Message
# modifiedSentence = clientSocket.recv(1024)
# print('From Server: ', modifiedSentence.decode())
# clientSocket.close()

