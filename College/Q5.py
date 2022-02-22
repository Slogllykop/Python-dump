A,B,C=input('Enter a 3 digit number: '),'The number is','an Armstrong number'
P,I=print,int
if I(A[0])**3+I(A[1])**3+I(A[2])**3==I(A):P(B,C)
else:P(B,'not',C)