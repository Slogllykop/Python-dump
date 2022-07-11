# https://www.codechef.com/submit/PROGLANG

t=int(input())
if t>=1 and t<=288:
    for i in range(t):
        w=list(map(int,input().split()))
        ab,a1b1,a2b2=list(w[0:2]),list(w[2:4]),list(w[4:6])
        ab.sort();a1b1.sort();a2b2.sort()
        for j in w:
            if j>=1 and j<=4:pass
            else:break
        if ab==a1b1:print(1)
        elif ab==a2b2:print(2)
        else:print(0)