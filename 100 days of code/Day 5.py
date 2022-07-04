# https://www.codechef.com/submit/CHEFAPPS

t=int(input())
if t>=1 and t<=1000:
    for i in range(t):
        s,x,y,z=map(int,input().split())
        if s>=1 and s<=500 and x>=1 and x<=s and y>=1 and y<=s and x<=y:
            if x+y<=s and z<=s:
                a=s-(x+y);b=s-y;c=s-x
                if a>=z:print(0)
                elif b>=z or c>=z:print(1)
                else:print(2)