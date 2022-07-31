# https://www.codechef.com/submit/PIZZA_BURGER

for _ in range(int(input())):
    x,y,z=map(int,input().split())
    if x<y and x<z:print("NOTHING")
    elif x>=y:print("PIZZA")
    else:print("BURGER")