P,I,M,R=print,int,input,range
for i in R(I(M())):
    A,C,E=I(M()),0,1;D=list(map(I,M().split()))
    if D[0]==D[1]:0
    else:C+=1
    while E<A-1:
        if D[E]==D[E+1] and D[E-1]==D[E]:E+=1
        else:C+=1;E+=1
    if D[-1]==D[-2]:0
    else:C+=1
    P(C)


# list=[]
# for a in range(1,100):
#     word=input()
#     n=int(input())
#     for i in range(0,n):
#         ele = input()
#         list.append(ele)
#     for x in range(0,n):
#         if list[i]!=word:
#             print(x+1)
#             break