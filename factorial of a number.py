A,B,P=int(input('Enter a number: ')),1,print
if A<0:P('Enter a positive number!')
elif A==0:P('Factorial of 0 is 1')
else:
	for i in range(1,A+1):B*=i
P(B)