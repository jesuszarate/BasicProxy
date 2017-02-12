import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("hash.cymru.com", 43))
s.send('f40581e27c69d18f8c12c1297622866e' + "\r\n")

response = ""
while True:
    data = s.recv(4096)
    response += data
    if not data:
        break
s.close()

print response