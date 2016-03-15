import time
import os
import httplib
import urllib
import random
import sys
import socket
import subprocess
from random import choice


# Colours
W  = "\033[0m";  
R  = "\033[31m"; 
G  = "\033[32m"; 
O  = "\033[33m"; 
B  = "\033[34m";


# Banner
def logo():
	print R+"\n|-------------------------------------------------------------------|"
        print "| www.trentchif.com                  THE MACHINE                        |"
        print "|             INSPIRED BY PERSON OF INTEREST                            |"
        print "|                                                                       |"
        print "|* * * * * * * * * * * * * W A R N I N G * * * * * * * * * * * * * * *  |"
        print "|This system is restricted to authorized users for authorized use only. |"
        print "|Unauthorized access is strictly prohibited and may be punishable under |"
        print "|the computer fraud and abuse act of 1986 or other applicable laws.     |"
        print "|If not authorized to access this system, disconnect now. By continuing,|"
        print "|you consent to your keystrokes and data content being monitored.       |"
        print "|All persons are hereby notified that the use of this system constitutes|"
        print "|consent to monitoring and auditing by the Administrator.               |"
        print "|* * * * * * * * * * * * * W A R N I N G * * * * * * * * * * * * * * ** |"
        print "|---------------------------------------------------------------------- |\n"
	print W

if sys.platform == 'linux' or sys.platform == 'linux2':
  subprocess.call("clear", shell=True)
  logo()
  
else:
  subprocess.call("cls", shell=True)
  logo()


print 'This Program is written by TRENT CHIF ,he is the admin of this programm'


site = raw_input("Web Site for Scan?: ")
site = site.replace("http://","")
print ("\tChecking website " + site + "...")
#checking the web to be online
conn = httplib.HTTPConnection(site)
#gettin the ip
o = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
conn.connect()
o.connect((site,80))
print "\t[$] Yes... Server is Online...." + time.ctime()
print        o.getsockname()

# this is anothoer function
u = urllib.urlopen('http://' + site)
data = u.read()
f = open('hacked.xml', 'wb')
f.write(data)
f.close()

print '========================================================================='
print ' Necessary component missing'
print ' Please run: bash %s -s' % os.path.abspath("setup/setup.sh")
print '========================================================================='
sys.exit()
