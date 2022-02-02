A=input('Enter a 3 digit number: ')
P,I=print,int
B=I(A[0])**3+I(A[1])**3+I(A[2])**3
if B==I(A):P('The number is an Armstrong number')
else:P('The number is not an Armstrong number')