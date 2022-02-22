I,P=input,print
while True:
    A,B=int(I('Enter a number: ')),1
    if A<0:P('Enter a Positive number!')
    elif A==0:P('Factorial of 0 is 1')
    else:
        for i in range(1,A+1):B*=i
        P(B)
    C=I('Do you want to find Factorial of another number? [Y/N]')
    if C=='N' or C=='n':break