# https://www.codechef.com/submit/TABLET

# for _ in range(int(input())):
#     n,b=map(int,input().split())
#     wt=[];ht=[];pt=[]
#     for i in range(n):
#         w,h,p=map(int,input().split())
#         if p>b:continue
#         else:wt.append(w);ht.append(h);pt.append(p)
#     if len(pt)==0:print("no tablet")
#     else:
#         a=[]
#         for j in range(len(pt)):a.append(wt[j]*ht[j])
#     print(max(a))

T = int(input())
for i in range(T):
    N, B = map(int,input().split())
    maxm = 0
    for j in range(N):
        W, H, P = map(int,input().split())
        if P<=B:
            maxm = max((W*H), maxm)
    if maxm:
        print(maxm)
    else:
        print("no tablet")