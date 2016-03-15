import time
import os
import sys
import random

def Main():
    print time.ctime()
    print 'what is your sex'
    choice = raw_input("what is your name (M)ale and (F)emale: ")

    if choice == 'M' :
        sex = raw_input("what is your name sex: ")
        print (" woll done ")        
        print time.ctime(time.time())

    elif choice == 'F' :
        print ("dako")
        print time.ctime(time.time()) 

    else:
        print ('thanx')
        print time.ctime(time.time())
        sex = raw_input("what is your name sex: ")

if __name__ == "__main__":
     Main() 
