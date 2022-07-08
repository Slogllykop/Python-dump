# https://www.codechef.com/submit/M1ENROL

t=int(input())
if t>=1 and t<=100:
    for i in range(t):
        x,y=map(int,input().split())
        if x>=1 and x<=(10**5) and y>=1 and y<=(10**5):
            if x>=y:print(0)
            else:print(abs(y-x))