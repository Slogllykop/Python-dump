from re import I
from socket import INADDR_ALLHOSTS_GROUP


A,B,C,D=int(input('Fibonacci upto how many terms?\n')),0,1,0
P=print
if A==1:P('Fibonacci sequence for 1 term is 0')
elif A<=0:P('Enter a positive integer and try again!')
else:
    P(f'Fibonacci sequesnce for the first {A} terms is:')
    while D<A:
        P(B);E=B+C;B=C;C=E;D+=1