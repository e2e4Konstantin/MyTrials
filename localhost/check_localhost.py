import socket
import sys
import pprint

print(socket.getaddrinfo("localhost", 0))

print(sys.executable)
print(sys.prefix)
print(sys.base_prefix)
pprint.pprint(sys.path)
