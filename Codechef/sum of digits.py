P,I,M,R,N=print,int,input,range,'Not valid'
A=M()
if A.isdigit():
    if I(A)<=1000 and I(A)>=1:
        for i in R(1,I(A)+1):
            C,D=[],M();B=len(D)
            if I(D)<=1000000 and I(D)>=1:
                for a in R(0,B):C.append(I(D[a]))
                P(sum(C))
            else:P(N)
    else:P(N)
else:P(N)