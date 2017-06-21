# your code goes here
import sys
def reverse(text):
	lst = []
	count = 1
	for i in range(0,len(text)):
		lst.append(text[len(text)-count])
		count += 1
	lst = ''.join(lst)
	return lst
for i in sys.stdin :
	string= i
ans = reverse(string)
print (ans)
