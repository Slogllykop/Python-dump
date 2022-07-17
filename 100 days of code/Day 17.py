# https://www.codechef.com/submit/GAMEOFPILES1

for i in range(int(input())):
    n,s=int(input()),list(map(int,input().split()))
    for j in s:
        if j==1:print("CHEF");break
    else:
        if sum(s)%2==0:print("CHEFINA")
        else:print("CHEF")
        
# for i in arr:
#         if(i==1):
#             print("CHEF")
#             break
#     else:
#         if(sum(arr)%2 == 0):
#             print("CHEFINA")
#         else:
#             print("CHEF")