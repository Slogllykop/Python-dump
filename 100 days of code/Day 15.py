# https://www.codechef.com/submit/MISSP

for i in range(int(input())):
    n=int(input());a=[]
    for j in range(n):
        b=int(input());a.append(b)
    for k in a:
        if a.count(k)%2!=0:print(k);break
