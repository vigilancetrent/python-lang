import sys
import time, math,random

def add(num1, num2):
    return num1 + num2
 
def sub(num1, num2):
    return num1 - num2
 
def mult(num1, num2):
    return num1 * num2
 
def div(num1, num2):
    return num1 / num2
 
def root(num1, num2):
    return num1 ** num2

def cose(num1):
    return num1


print time.ctime()

print '\n','-'* 2

print '1.ADD'
print '2.SUBTRACTION'
print '3.DIV'
print '4.MULT'
print '5.root'
print '6.cose'
print '\n'*2
print ' ----------------------START---------------------------------- '

choice =raw_input('choice any on top ((1) and (2) and (3) and (4) and (5) and (6)):', )
print'\n'*2
num1 = int(input('ENTER FIRST NUMBER...:', ))
num2 = int(input('ENTER SECOND NUMBER..:', ))
print'\n'*2

if choice == '1':

   print time.ctime()
   print'\n'*2
   sum = (num1, '+', num2, '=', add(num1,num2))
   print sum

elif choice == '2':

   print time.ctime()
   print'\n'*2
   sum = (num1, '-', num2, '=', sub(num1,num2))
   print sum

if choice == '3':

   print time.ctime()
   print'\n'*2
   sum = (num1, '/', num2, '=', div(num1,num2))
   print sum

if choice == '4':

   print time.ctime()
   print'\n'*2
   sum = (num1, '*', num2, '=', mult(num1,num2))
   print sum

if choice == '5':

   print time.ctime()
   print'\n'*2
   sum = (num1, '**', num2, '=', root(num1,num2))
   print sum

if choice == '6':

   print time.ctime()
   print'\n'*2
   num1 = math.cos(input('ENTER COSE NUMBER:', ))
   print num1

else:
    time.sleep(10)


