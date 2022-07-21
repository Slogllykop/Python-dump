# https://www.codechef.com/submit/AIRLINE

def g(x,y,z,w,v):
    counter=0
    l,m,n=x+y,y+z,z+x
    if l<=w and z<=v:counter=1
    elif m<=w and x<=v:counter=1
    elif n<=w and y<=v:counter=1
    return counter

for _ in range(int(input())):
    a,b,c,d,e=map(int,input().split())
    h=g(a,b,c,d,e)
    if h:print("YES")
    else:print("NO")