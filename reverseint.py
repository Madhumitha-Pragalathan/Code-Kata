import sys
def reverseDigits(num):
	rev_num = 0
	while(num > 0):
		rev_num = rev_num*10 + num%10
		num = num/10
	return rev_num
for i in sys.stdin :
	num1 = i 
num2 = int(num1)
ans = reverseDigits(num2)
print (ans)
