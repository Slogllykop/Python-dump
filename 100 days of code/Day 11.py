# https://www.codechef.com/submit/GRPASSN

t=int(input())
if t>=1 and t<=1000:
    for i in range(t):
        n=int(input())
        p=list(map(int,input().split()))
        for k in range(3):
            for j in p:
                if j>n:break
                a=p.count(j)
                if a==j:
                    try:
                        while True:p.remove(j)
                    except ValueError:pass
                elif a>j:
                    try:
                        for l in range(j):p.remove(j)
                    except ValueError:pass
        if p:print("NO")
        else:print("YES")