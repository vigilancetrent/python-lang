# Sockets client script
import socket, time

s = socket.socket()
print("Connecting to server...")
while True:
    try:
        s.connect((" ", 50000))
        break
    except:
        print("Retrying connection to server...")
        time.sleep(1)

print("Connection Matched!")

while True:
      keyboardInput = input("Enter the message: ")
      # s.send(bytes(message, 'UTF-8'))
      message = keyboardInput.encode('utf-8')
      s.send(message)
      print("Message sent!")
      r = s.recv( 128)
      a = r.decode('utf-8')
      print("Confirmation received message: ", a)
      if keyboardInput == "quit":
         break

print("Good bye")

s.close()

a = input("Enter key to End:")
