# https://www.codechef.com/submit/MUFFINS3

for _ in range(int(input())):
    n=int(input())
    # l=n-((n-1)/2)
    if n%2==0:print(int(n/2)+1)
    else:print(int(n-((n-1)/2)))