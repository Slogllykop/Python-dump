# https://www.codechef.com/submit/EQUALSTRING

for _ in range(int(input())):
    n=int(input());a=input();b=input()
    d=[]
    for i in range(n):
        if b[i]!=a[i]:d.append(b[i])
    print(len(set(d)))