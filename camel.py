import sys
for i in sys.stdin :
string = i
print (string)
l = string.split("_")
print (l)
print (" ".join(map(str.capitalize, l[0:])))
