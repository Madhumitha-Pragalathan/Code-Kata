# your code goes here
import sys
for i in sys.stdin :
	a = i
a = int(a)
visited = set()
while 1:
    if a == 1:
        print ("Happy Number")
        break
    a = sum(int(c) ** 2 for c in str(a))
    if a in visited:
        print ("Not a Happy Number")
        break
    visited.add(a)
