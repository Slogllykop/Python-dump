# https://www.codechef.com/submit/ENDSORTED

for i in range(int(input())):
    n,p=int(input()),list(map(int,input().split()))
    i1,iN=0,0
    for j in range(n):
        if p[j]==1:i1=j
        elif p[j]==n:iN=j
    d=i1+(n-1)-iN
    if i1<iN:print(d)
    else:print(d-1)