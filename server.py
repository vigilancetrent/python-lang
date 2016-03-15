# Sockets server.
import socket

s = socket.socket()
s.bind(("localhost", 444))
s.listen(9)

print("Connection Waiting...")
sc, addr = s.accept()
print("Connection Matched!")

while True:
    print("Waiting message...")
    received = sc.recv(128)
    print(type(received))
    a = received.decode('utf-8')
    print(type(a), len(a))
    if a == "quit":
        break
    print("Received Message:", a)
    sc.send(received)

print("Good bye!")

sc.close()
s.close()
a = input("Enter key to End:")
