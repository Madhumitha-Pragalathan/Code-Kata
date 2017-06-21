import sys
for i in sys.stdin :
	num1 = i
	break
for i in sys.stdin :
	num2 = i
	break
for i in sys.stdin :
	num3 = i
	break
if(num1 > num2) and (num1 > num3) :
	num1 = str(num1)
	num2 = str(num2)
	num3 = str(num3)
	print (num1+" is greater than "+num2+" and"+num3)
elif(num2 > num1) and (num2 > num3) :
	num1 = str(num1)
	num2 = str(num2)
	num3 = str(num3)
	print (num2+" is greater than "+num1+" and"+num3)
else:
	num1 = str(num1)
	num2 = str(num2)
	num3 = str(num3)
	print (num3+" is greater than "+num1+" and"+num2)
	
