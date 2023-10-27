str1=input("Enter a string")
str2=input("Enter another string")

def anagram(str1,str2):
	str3=str1.lower()
	string=str3.replace(" ","")
	if string==str2:
		print(str2,"is anagram of", str1)
	else:
		print(str2,"is not anagram of", str1)
anagram(str1,str2)