numb1=int(input("enter first number:"))
numb2=int(input("enter second number:"))
oper=input("enter the operator:")

if oper=="+":
	ans=numb1+numb2
	print(ans)

elif oper=="-":
	ans=numb1-numb2
	print(ans)

elif oper=="*":
	ans=numb1*numb2
	print(ans)

elif oper=="/":
	ans=numb1/numb2
	print(ans)

elif oper=="%":
	ans=numb1%numb2
	print(ans)

elif oper=="//":
	ans=numb1//numb2
	print(ans)

elif oper=="**":
	ans=numb1**numb2
	print(ans)
else:
	print("you have given wrong operator")






