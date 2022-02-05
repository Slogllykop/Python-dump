A,B=map(int,input('Enter start and end year: ').split())
for i in range(A,B):
    if (0 == i % 4) and (0 != i % 100) or (0 == i % 400):print (i,'',end='')