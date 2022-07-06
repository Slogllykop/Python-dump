# https://www.codechef.com/submit/TEA

t=int(input())
if t>=1 and t<=1000:
    for i in range(t):
        w=list(map(int,input().split()))
        x,y,z=w[0],w[1],w[2]
        if x>=1 and y>=1 and z>=1 and x<=100 and z<=100:
            a=1
            while True:
                if (x-y)<1:break
                else:y+=w[1]
                a+=1
            print(a*z)