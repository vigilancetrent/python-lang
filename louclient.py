#client
import socket
import time

HOST = "localhost"
PORT = 5454
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((HOST,PORT))
while True:

      data = raw_input("Enter..... ")
      s.sendto(data,(Host,PORT))

      print "Server says: " + s.recv(1024)

      if data=="bye" or s.recv(1024)=="bye":
           print "Exiting..........."
           time.sleep(1)
           break
