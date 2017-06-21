import sys
for i in sys.stdin :
	num = i
n = int(num)
count=0
while(n>0):
    count=count+1
    n=n//10
print("The number of digits in the number are:",count)
