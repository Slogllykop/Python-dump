P,I,M,R,N=print,int,input,range,'Not valid'
A=I(M())
if A<=100 and A>=1:
    for i in R(A):
        B=I(M())
        if B<=1000 and B>=2:
            if B%4==0 or B%4==1:P('NO')
            elif B:P('YES')
        else:P(N)
else:P(N)