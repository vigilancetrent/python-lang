<frame width="560"hright=315"src="channel/"frameborde="0"allowfullscreen></iframe>
import os
import time
import random
import sys
import datetime


def main():
   log = raw_input('ENTER THE TXT HERE:', )
   f = open('log.txt', "r")
   data = f.read()
   print data 

   print time.ctime()
   g = open('log.txt', "w")
   write = raw_input('ENTER THE IN PUT:', )
   print time.ctime()
   write = g.write(raw_input('ENTER ACCOUNT:', ))
   print time.ctime()

if __name__ == '__main__':
      main()




