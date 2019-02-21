from socket import *
from googletrans import Translator
import json

# This function was implemented using googletrans
# a unofficial Google Translate library
def my_translator(text, src_lang, dest_lang):

    translator = Translator()
    translation = translator.translate(
        text=text,
        src=src_lang,
        dest=dest_lang
    )
    return translation.origin + ' -> ' + translation.text


# Setting up the server
my_host = ''
my_port = 50001

# This is a TCP/IP server
server_tcp = socket(AF_INET, SOCK_STREAM)
origin = (my_host, my_port)
server_tcp.bind(origin)
server_tcp.listen(1)

# Running server
while True:
    connection, client = server_tcp.accept()
    print('Connected by: ', client)
    
    while True:
        message = connection.recv(1024)
        if not message:
            connection.send(b'Empty message') 
            break
        
        # The server recieves a JSON object and
        # convert it in a dict object
        dic = json.loads(message.decode())
        
        response = my_translator(
            dic["text"],
            dic["src_lang"],
            dic["dest_lang"]
        )

        connection.send(response.encode())
    
    print('Close connection')
    connection.close()
