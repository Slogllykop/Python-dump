# https://www.codechef.com/submit/AGELIMIT

T=int(input())
for i in range(T):
    x,y,a=map(int,input().split())
    if a>=x and a<y:print("YES")
    else:print("NO")