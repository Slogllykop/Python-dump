P=print
A=list(map(int,input('Enter all marks seperated with spaces: ').split())) 
M=sum(A)/5
if A[0]<40 or A[1]<40 or A[2]<40 or A[3]<40 or A[4]<40:P('Failed',f'\nAggregate score is: {M}%')
elif M>=75:P('Distinction',f'\nAggregate score is: {M}%')
elif M>=60:P('First class',f'\nAggregate score is: {M}%')
elif M>=50:P('Second class',f'\nAggregate score is: {M}%')
else:P('Thrid class',f'\nAggregate score is: {M}%')