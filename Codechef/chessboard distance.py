P,I,M,R,A=print,int,input,range,abs
for i in R(I(M())):
    X1,Y1,X2,Y2=map(I,M().split())
    P(max(A(X1-X2),A(Y1-Y2)))