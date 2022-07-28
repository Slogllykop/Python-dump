# https://www.codechef.com/submit/FODCHAIN

for _ in range(int(input())):
    e,k=map(int,input().split())
    c=0
    if e<k:print(1)
    elif e==k:print(2)
    else:
        while True:
            if e!=0:e//=k;c+=1
            else:break
        print(c)