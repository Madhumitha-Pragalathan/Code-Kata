import sys
for i in sys.stdin :
	y = i
year = int(y)
if(year % 400 == 0):
  year = str(year)
  print ("Year "+year+" is leap")
elif(year % 100 == 0):
  year = str(year)
  print ("Year "+year+" is not leap")
elif(year % 4 == 0):
  year = str(year)
  print ("Year "+year+" is leap")
else:
  year = str(year)
  print ("Year "+year+" is not leap")
