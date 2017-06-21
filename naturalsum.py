import sys
#n=input("Enter a number: ")
for i in sys.stdin :
	num  = int(i)
res = 0
for i in range(0,num):
  res = res+ num
  num = num - 1
print ("The sum of first n natural numbers is",res)
