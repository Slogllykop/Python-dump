# https://www.codechef.com/submit/CNDLOVE

for _ in range(int(input())):
    n=input();l=list(map(int,input().split()))
    if sum(l)%2==0:print('NO')
    else:print('YES')