# https://www.codechef.com/submit/BURGERS2

for _ in range(int(input())):
    x,y,n,r=map(int,input().split())
    if r<(n*x):print(-1)
    else:
        b=(r-(n*x))//(y-x);a=n-b
        if (n*y)<=r:print(0,n)
        else:print(a,b)