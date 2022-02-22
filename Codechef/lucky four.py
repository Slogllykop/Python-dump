P,I,M,R,N=print,int,input,range,'Invalid'
A=M()
if A.isdigit():
    if I(A)<=10**5 and I(A)>=1:
        for i in R(I(A)):
            C,D=[],M();B=len(D)
            if I(D)<=10**9 and I(D)>=1:
                for a in R(B):C.append(I(D[a]))
                E=C.count('4');P(E)
            else:P(N)
    else:P(N)
else:P(N)