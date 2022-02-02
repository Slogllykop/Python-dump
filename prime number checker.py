A=int(input('Enter a number: '))
B,P=True,print
for i in range(2,A):
    if A%i==0:B=False;break
if B:P('Prime')
else:P("Not Prime")