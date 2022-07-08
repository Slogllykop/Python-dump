# https://www.codechef.com/submit/ACCURACY

t=int(input())
if t>=1 and t<=100:
    for i in range(t):
        x=int(input())
        if x>=0 and x<=100:
            if x%3==0:print(0)
            else:
                a=(x//3)+1;b=x-(a*3)
                print(abs(b))