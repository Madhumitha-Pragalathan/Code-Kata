import sys
for i in sys.stdin :
	num = i
n = int(num)
def fact(n) :
	if n == 1 :
		return 1
	elif n == 2 :
		return 2 
	else :
		return n*fact(n-1)
ans = fact(n)
print(ans)
		
