str = (input("Enter a String"))
def count_chr(str):
	count = 0
	for i in str:
		count+= 1
	return count
count=count_chr(str)
print(count," letters are present")

