# louis
# best

import os
import time
import random
import sys
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
	print R+"\n|---------------------------------------------------------------|"
        print "| www.trentchif.com                  THE MACHINE                        |"
        print "|             INSPIRED BY PERSON OF INTEREST                           |"
        print "|                                                                       |"
        print "|* * * * * * * * * * * * * W A R N I N G * * * * * * * * * * * * * * *  |"
        print "|This system is restricted to authorized users for authorized use only.|"
        print "|Unauthorized access is strictly prohibited and may be punishable under|"
        print "|the computer fraud and abuse act of 1986 or other applicable laws.|"
        print "|If not authorized to access this system, disconnect now. By continuing,|"
        print "|you consent to your keystrokes and data content being monitored.|"
        print "|All persons are hereby notified that the use of this system constitutes|"
        print "|consent to monitoring and auditing by the Administrator.|"
        print "|* * * * * * * * * * * * * W A R N I N G * * * * * * * * * * * * * * **|"
        print "|---------------------------------------------------------------|\n"
	print W

if sys.platform == 'linux' or sys.platform == 'linux2':
  subprocess.call("clear", shell=True)
  logo()
  
else:
  subprocess.call("cls", shell=True)
  logo()

def Main():
    print 'This Program is written by TRENT CHIF ,he is the admin of this programm'

    print ('\n')

    statements = ['DATE SAT-04-NOVEMBER-2015', 'THIS IS THE CURRENT TIME', time.ctime(), 'THIS IS MY FIRST PROGRAM', 'INSPIRED BY PERSON OF INTEREST']

    for y in statements:
        print(y)

    print time.ctime()

    print ('\n' * 2 )

    print ('..........................WHAT IS YOUR NAME ...............................')
    name = sys.stdin.readline()

    print 'HELLO', name
    print '...........................WELLCOME TO THE MAIN SECTION .....................'

    print ('\n' * 2 )
     
    message = raw_input('Are you (ADMIN) or (GUEST): ')
    print message

    if message == 'ADMIN':

       print '.......WELLCOME TO THE ADMIN SECTION......', time.ctime() 
       randomNumber = 17031993
       found = False

       while not found:
           password = input('ADMIN PASSWORD: ')
           if password == randomNumber:
               print 'PASSWORD GRANTED'
               print ('\n' * 2 )

               print '........WELLCOME YOU ARE NOW LOGGED IN AS THE ADMIN...............'
               print time.ctime()
               found = True
           else:
               print 'PASSWORD BLOCKED'
    else:
        print time.ctime()
        print 'WELLCOME TO THE GUEST ACCOUNT'
        print ('\n' * 2 )
        print 'ACCESS GRANTED'
        print ('\n' * 3 )
        print 'LETS START CREATING YOUR PERSONAL ACCOUNT'

        print 'first and last name'
        name1 = sys.stdin.readline()
        print 'first and last name', name1

        print 'email address'
        email = sys.stdin.readline()
        print 'email address', email

        print 'phone number'
        number = sys.stdin.readline()
        print 'phone number', number

        print 'sex'
        name2 = sys.stdin.readline()
        print 'sex', name2

        print ('\n' * 2 )

        print 'I WANT TO PLAY A GAME WITH YOU WILL YOU ALLOW ME'
        print time.ctime()
        print 'LET US START'
        print ('\n' * 2 )

        print 'CHOOSE ANY NUMBER BETWEEN (1) AND (9)'
        print ('\n' * 2 )

        print 'number'
        number1 = sys.stdin.readline()
        print 'number', number1

        print ('\n' * 2 )
        print 'MULTIPLY THE NUMBER WITH (9) OR NINE'
        print ('\n' * 2 )

        print 'ENTER THE ANSWER HERE'        
        answer = sys.stdin.readline()
        print 'ENTER THE ANSWER HERE', answer

        print ('\n' * 2 )
        print 'DEVIDE THE NUMBER WITH (9)'
        answer1 = sys.stdin.readline()
        print 'ANSWER AFTER DIVISION', answer1
        print '\n' * 2 

        print 'SUBTRACT (5) FROM THE ANSWER'
        print ('\n' * 2 )

        print 'ENTER HERE THE ANSWER YOU HAVE SUBTRACTED FROM ...'
        answer2 = sys.stdin.readline()
        print 'ENTER HERE THE ANSWER YOU HAVE SUBTRACTED FROM ...', answer2
        print ('\n' * 2 )

        print 'FROM ALPHABETICAL CHOOSE A LETTER REPRESENTED BY THAT NUMBER'
        print '......................................................................'

        print 'ENTER HERE THE LETTER ...'
        answer2 = sys.stdin.readline()
        print 'ENTER HERE THE LETTER ...', answer2
        print ('\n' * 2 )

        print 'FOR THAT LETTER CHOOSE A COUNTRY THAT START WITH THAT LETTER'
        print '.......................................................................'

        print 'ENTER HERE THE COUNTRY ...'
        answer2 = sys.stdin.readline()
        print 'ENTER HERE THE COUNTRY ...', answer2
        print ('\n' * 2 )

        print 'SECOND LETTER OF THAT COUNRTY YOU CHOOSE , CHOOSE AN ANIMAL THAT START WITH THE LETTER'

        print 'ENTER HERE THE ANIMAL ...'
        answer2 = sys.stdin.readline()
        print 'ENTER HERE THE ANIMAL ...', answer2
        print ('\n' * 2 )

        print 'THE COMPUTER IS GOING TO GIVE YOU THE ANSWER .......... LOADING........'

        print 'ENTER YES TO CONTINUE ...'
        answer2 = sys.stdin.readline()
        print 'ENTER YES TO CONTINUE ...', answer2
        print ('\n' * 2 )

        print 'PLEASE WAIT WHILE WE PROCESS YOUR REQUEST ....'
        print time.ctime()
        print '......................................................................>'
        print 'PLEASE.........................................>........>..............'
        print 'WAIT............>.................................>....................'
        print 'WHILE..................................................................'
        print 'LOADING.......................................................>>>>>>>>>'
        print ('\n' * 4 )

        print 'ENTER LOAD DATA ...'
        answer2 = sys.stdin.readline()
        print 'ENTER LOAD DATA ...', answer2

        print '====.>  ===>  ====>  ====> =====> ======>  =======> =========> =======>'
        print '=================> =====================>  ==========================> '
        print '======================================================================='
        print '===============================================================>       '
        print '===============>         ==========================================>   '
        print 'YOUR ANSWER IS .......................................................'
        print '.......................................................................'

        print 'PLEASE ENTER (YES) TO DISPLAY YOUR ANSWER ...'
        answer2 = sys.stdin.readline()
        print 'PLEASE ENTER (YES)TO DISPLAY YOUR ANSWER ...', answer2

        print ('\n' * 2 )
        print time.ctime()
        print '          ELEPHANT......>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>'

        print 'IS IT TRUE TYPE (YES) ...'
        answer2 = sys.stdin.readline()
        print 'IS IT TRUE TYPE (YES) ...', answer2
        print ('\n' * 2 )

        print '................ i won ........'
        print ('\n' * 2 )

        print ' logout'
        print ('\n' * 2 )

        print 'LOGOUT FROM THE GUEST ACCOUNT  (YES) '
        logout = sys.stdin.readline()
        print 'LOGOUT FROM THE GUEST ACCOUNT', logout   

if __name__ == '__main__':
   Main()  














           














