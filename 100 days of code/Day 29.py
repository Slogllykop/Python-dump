# https://www.codechef.com/submit/VALIDMIN

for _ in range(int(input())):
    a,b,c=map(int,input().split());m=min
    if m(a,b)==m(b,c) and m(a,b)==m(c,a):print("YES")
    else:print("NO")