from socket import *
import json

server_host = 'localhost'
server_port = 5001

client_tcp = socket(AF_INET, SOCK_STREAM)
destination = (server_host, server_port)
client_tcp.connect(destination)

count = 0
dic = {}

print("Type the word what you may translate")
print("the source language and the destination language")
while count < 3:
    text = input().split()
    dic[text[0]] = text[1]
    count += 1

message = json.dumps(dic).encode()
client_tcp.send(message)

client_tcp.close()
