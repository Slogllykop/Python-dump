# https://www.codechef.com/submit/ELECTIONS

for _ in range(int(input())):
    x=list(map(int,input().split()))
    c=""
    for i in range(len(x)):
        if x[i]>50:
            if i==0:c="A"
            elif i==1:c="B"
            elif i==2:c="C"
    if c=="":print("NOTA")
    else:print(c)