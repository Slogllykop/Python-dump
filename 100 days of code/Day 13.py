# https://www.codechef.com/submit/SLOWSOLN

t=int(input())
for i in range(t):
    x,y,z=map(int,input().split())
    s=0
    while x and z:
        m=min(y,z)
        s+=m*m;x-=1;z-=m
    print(s)