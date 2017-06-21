# your code goes here
import sys
for i in sys.stdin :
	c = i
count = int(c)
for num in range(1,count):
    prime = True
    for i in range(2,num//2):
        if (num%i==0):
            prime = False
    if prime:
       print (num)
