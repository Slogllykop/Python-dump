def add(a,b):return a+b
def sub(a,b):return a-b
def mul(a,b):return a*b
def div(a,b):return a/b
def exp(a,b):return a**b
def fac(a):
    A=1
    for i in range(a, 0, -1):A*=i
    return A
F,M,P,I,S,H=float,map,print,input,'Enter two numbers: ','Answer: '
while True:
    Z=I('Operations available:\n1 - Add\n2 - Subtract\n3 - Multiply\n4 - Divide\n5 - Exponentiation\n6 - Factorial\nEnter the operation index: ')
    if Z.isdigit():
        if Z=='1':B,C=M(F,I(S).split());P(H,add(B,C))
        elif Z=='2':B,C=M(F,I(S).split());P(H,sub(B,C))
        elif Z=='3':B,C=M(F,I(S).split());P(H,mul(B,C))
        elif Z=='4':B,C=M(F,I(S).split());P(H,div(B,C))
        elif Z=='5':B,C=M(F,I(S).split());P(H,exp(B,C))
        elif Z=='6':B=int(I('Enter a number: '));P(H,fac(B))
    else:P('Invalid')
    D=I('Do you want to do another calculation? [Y/N]: ')
    if D=='N' or D=='n':break