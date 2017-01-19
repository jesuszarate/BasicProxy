from socket import *

serverPort = 12000

serverSocket = socket(AF_INET, SOCK_STREAM)

serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print ('The server is ready to receive')

while 1:
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(1024).decode()
    print('Received message.')
    print('Converting to upper case...')
    capitalizesSentence = sentence.upper()
    print('Converted', sentence, ' to upper case.')
    print ('Sending message...')
    connectionSocket.send(capitalizesSentence.encode())
    print ('Message sent.')
    print ('Closing socket...')
    connectionSocket.close()
    print ('Socket closed!')


