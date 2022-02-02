A=list(map(int,input('Enter the numbers : ').split())) 
A.sort()
B=sum
print('Minimum number:',A[0],'\nMaximum number:',A[-1],'\nSum of the numbers:',B(A),'\nAverage of the numbers:',B(A)/len(A))