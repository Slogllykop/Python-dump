import random as R
I,P=int,print
E=20
B=I(E*R.random()+1)
A=0
while A!=B:
	A=I(input('Enter the number: '))
	if A>0:
		if A>B:P('Number is too large!')
		elif A<B:P('Number is too small!')
	else:P('Sorry, you lost the game!')
else:P('Congratulations! You won the game!')