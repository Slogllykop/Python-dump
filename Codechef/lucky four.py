P,I,M,R,N=print,int,input,range,'Not valid'
A=M()
if A.isdigit():
    if I(A)<=100000 and I(A)>=1:
        for i in R(I(A)):
            C,D=[],M();B=len(D)
            if I(D)<=(10)**9 and I(D)>=0:
                for a in R(B):C.append(D[a])
                P(C.count("4"))
            else:P(N)
    else:P(N)
else:P(N)

# tc=int(input())
# for i in range(tc):
#     count=0
#     num=int(input())
#     while num:
#         a=num%10
#         if a==4:
#             count+=1
#         num=int(num/10)
#     print(count)


