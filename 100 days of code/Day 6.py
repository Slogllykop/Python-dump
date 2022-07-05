# https://www.codechef.com/submit/ATM2

t=int(input())
if t>=1 and t<=100:
    for i in range(t):
        n,k=map(int,input().split())
        if n>=1 and n<=100 and k>=1 and k<=1000000:
            a=list(map(int,input().split()))
            for j in range(n):
                if a[j]<=k:
                    print(1,end='')
                    k-=a[j]
                else:
                    print(0,end='')
            print()