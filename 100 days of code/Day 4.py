# https://www.codechef.com/submit/CHANGEPOS

for i in range(int(input())):
    a,b,x,y=map(int,input().split())
    if a!=x and b!=y:print(1)
    else:print(2)  