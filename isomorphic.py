# your code goes here
import sys
for i in sys.stdin :
	s1 = i
	break
for i in sys.stdin :
	s2 = i
m = len(s1)
n = len(s2)
if(m !=n):
	ans = 'false'
else :
	map = {}
	visit = []
	for i in range(m):
		if (s1[i] not in map.keys()):
			if (s2[i] not in visit):
				map[s1[i]] = s2[i]
				visit.append(s2[i])
			else:
				ans = 'false'
		elif(map[s1[i]] != s2[i]):
				ans = 'false'
	ans = 'true'
print (ans)
