def reverse(text):
	lst = []
	count = 1
	for i in range(0,len(text)):
		lst.append(text[len(text)-count])
		count += 1
	lst = ''.join(lst)
	return lst
string = str(input("Enter the string"))
ans = reverse(string)
print (ans)
vowels = ('a','e','i','o','u','A','E','I','O','U')
m = len(ans)
for c in ans :
  if c in vowels :
    ans = ans.replace(c,"")
print (ans)
