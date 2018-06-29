import socket, ssl

bindsocket = socket.socket()
bindsocket.bind(('', 10024))
bindsocket.listen(5)

newsocket, fromaddr = bindsocket.accept()
connstream = ssl.wrap_socket(newsocket,
                             server_side=True,
                             certfile="server.crt",
                             keyfile="server.key")

data = connstream.read(2)
print data
connstream.write("haha")

connstream.close()