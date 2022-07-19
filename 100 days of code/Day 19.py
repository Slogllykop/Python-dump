# https://www.codechef.com/submit/EZSPEAK

for _ in range(int(input())):
    n=int(input());s=input()
    l=['a','e','i','o','u']
    c=0
    for i in range(n):
        if s[i] not in l and i<(n-3):
            c=0
            for j in range(4):
                if  s[j+i] not in l:c+=1
            if c==4:break
    if c==4:print("NO")
    else:print("YES")