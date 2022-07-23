# https://www.codechef.com/submit/BREAKSTICK

def z(n):return n%2
for _ in range(int(input())):
    n,x=map(int,input().split())
    if z(n)==0 or z(x)==1:print('YES')
    else:print('NO')