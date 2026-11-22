num=int(input("Enter num "))
res=1
for i in range(1,num+1):
	res*=i
isprime=True
for i in range(2,num):
	if num%i==0:
		isprime=False
		break
print(f"factorial of {num} is {res} ")
if(isprime):
	print(f"{num} is prime no ")
else:
	print(f"{num} is not prime no ")	
	//s
