A,B=map(int,input('Enter start and end year: ').split())
for i in range(A,B+1):
    if i%4==0 and i%100!=0 or i%400==0:print(i,'',end='')