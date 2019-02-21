from socket import *
import json

# Setting up connection to the server
server_host = 'localhost'
server_port = 50001

# Creating a socket and estabilishing connection
client_tcp = socket(AF_INET, SOCK_STREAM)
destination = (server_host, server_port)
client_tcp.connect(destination)

count = 0
dic = {}

# main
print("Type the word what you may translate")
print("the source language and the destination language")
while count < 3:
    text = input().split()
    dic[text[0]] = text[1]
    count += 1

message = json.dumps(dic).encode()
client_tcp.send(message)

response = client_tcp.recv(1024).decode()

print()
print("Translated: " + response)

client_tcp.close()
