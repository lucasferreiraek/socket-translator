from socket import *
import json

# Setting up connection to the server
server_host = 'localhost'
server_port = 50001

# Creating a socket and estabilishing connection
client_tcp = socket(AF_INET, SOCK_STREAM)
destination = (server_host, server_port)
client_tcp.connect(destination)

msg = {}
keys = ['text', 'src_lang', 'dest_lang']

# main
while True:
    print("Welcome to the Socket Translator")
    print("To translate some word, type 'y'")
    print("To exit type any button")
    code = input()
    
    if (code == 'y'):
        print("The languages are indentified by abbreviations:")
        print("pt = portuguese; en = english; japanese = jp, es = spanish")
        print("==============================================================")
        print("In this following sequence:")
        print("1) Type the word what you wish translate")
        print("2) Type the source language")
        print("3) Type the destination language")

        msg_in = input().split()
        for key, word in zip(keys, msg_in):
            msg[key] = word

        message = json.dumps(msg).encode()
        client_tcp.send(message)

        response = client_tcp.recv(1024).decode()

        print()
        print("Translated: " + response + '\n')
    else:
        client_tcp.close()
        print("Falou!!!")
        break
