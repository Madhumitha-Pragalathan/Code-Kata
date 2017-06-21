# your code goes here
import sys
for i in sys.stdin :
	char = i
if(char >='a' and char <= 'z') or (char >= 'A' and char <= 'Z'):
	print ("Alphabet")
else:
	print("Not an alphabet")
