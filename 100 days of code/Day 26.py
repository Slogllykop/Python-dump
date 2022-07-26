# https://www.codechef.com/submit/MASKPOL

for _ in range(int(input())):
    n,a=map(int,input().split())
    d=n//2
    if d==a:print(a)
    elif d<a:print(n-a)
    elif d>a:print(a)