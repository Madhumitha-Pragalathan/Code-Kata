n = input("Enter the number of terms")
num = int(n)
sum=0
l = []
for i in range(1,num+1):
  l.append(i)
print (l)
for element in l:
    sum+=element
print (sum)
