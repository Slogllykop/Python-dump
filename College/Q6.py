I,F,M,P,N=int, float, map, print, input
X,Y='Enter two numbers: ','Enter a valid index'
Z=N('Operations available:\n1 - Add\n2 - Subtract\n3 - Multiply\n4 - Divide\n5 - X^Y\n6 - X!\nEnter the operation index: ')
if Z.isdigit():
    if I(Z)==1:A,B=M(F,N(X).split());P(A+B)
    elif I(Z)==2:A,B=M(F,N(X).split());P(A-B)
    elif I(Z)==3:A,B=M(F,N(X).split());P(A*B)
    elif I(Z)==4:A,B=M(F,N(X).split());P(A/B)
    elif I(Z)==5:A,B=M(F,N(X).split());P(A**B)
    elif I(Z)==6:
        A,B=I(N('Enter a number to find the factorial: ')),1
        while A!=0:B*=A;A-=1
        P(B)
    else:P(Y)
else:P(Y)


