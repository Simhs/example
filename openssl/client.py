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