# telnet program example
import socket, select, string, sys
import subprocess
import time
from random import choice

# Colours
W  = "\033[0m";  
R  = "\033[31m"; 
G  = "\033[32m"; 
O  = "\033[33m"; 
B  = "\033[34m";


# Banner
def logo():
	print R+"\n|---------------------------------------------------------------|"
        print "| www.trentchif.com                  THE MACHINE                |"
        print "|     INSPIRED BY PERSON OF INTEREST                            |"
        print "|                                                               |"
        print "|---------------------------------------------------------------|\n"
	print W

if sys.platform == 'linux' or sys.platform == 'linux2':
  subprocess.call("clear", shell=True)
  logo()
  
else:
  subprocess.call("cls", shell=True)
  logo()

 
def promt():
    
    message = sys.stdout.write('you->')
    sys.stdout.flush()   
 
#main function
if __name__ == '__main__':

    print time.ctime() 

    host = '192.168.0.103'
    port = 443
     
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(2)
     
    # connect to remote host
    try :
        s.connect((host, port))
    except :
        print 'Unable to connect'
        sys.exit()
     
    print 'Connected to remote host. Start sending messages'
    promt()
     
    while 1:
        socket_list = [sys.stdin, s]
         
        # Get the list sockets which are readable
        read_sockets, write_sockets, error_sockets = select.select(socket_list , [], [])
         
        for sock in read_sockets:
            #incoming message from remote server
            if sock == s:
                data = sock.recv(4096)
                if not data :
                    print '\nDisconnected from chat server'
                    sys.exit()
                else :
                    #print data
                    sys.stdout.write(data)
                    promt()
             
            #user entered a message
            else :
                msg = sys.stdin.readline()
                s.send(msg)
                promt()
                
