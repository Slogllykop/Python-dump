for j in range(int(input())):
    A,C=int(input()),0
    for i in range(11,-1,-1):
        B=2**i
        while A>=B:A-=B;C+=1
    print(C)

# for j in range(int(input())):
#     price=int(input())
#     count=0
#     for i in range(11,-1,-1):
#         billpower=2**i
#         while price>=billpower:
#             price-=billpower
#             count+=1
#     print(count)