openssl pyhton 예제

```shell
~$ openssl genrsa -des3 -out server.orig.key 2048
~$ openssl rsa -in server.orig.key -out server.key
~$ openssl req -new -key server.key -out server.csr
~$ openssl x509 -req -days 365 -in server.csr -signkey server.key -out server.crt
```

#serv.py
```python
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
```

#client.py

```python
import socket, ssl, pprint

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Require a certificate from the server. We used a self-signed certificate
# so here ca_certs must be the server certificate itself.
ssl_sock = ssl.wrap_socket(s,
                           ca_certs="server.crt",
                           cert_reqs=ssl.CERT_REQUIRED)

ssl_sock.connect(('localhost', 10024))

print repr(ssl_sock.getpeername())
print ssl_sock.cipher()
print pprint.pformat(ssl_sock.getpeercert())

ssl_sock.write("12")
data = ssl_sock.read(2)
print data
ssl_sock.close()
```
