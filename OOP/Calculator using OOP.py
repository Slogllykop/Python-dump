class Calculator:
    def __init__(self,a,b):self.a=a;self.b=b
    def add(self):return self.a+self.b
    def sub(self):return self.a-self.b
    def div(self):return self.a/self.b
    def mul(self):return self.a*self.b
    def exp(self):return self.a**self.b
    def fac(self):
        A=1
        for i in range(self.a, 0, -1):A*=i
        return A
P,I,H=print,input,'Answer: '
while True:
    def C():a,b=map(float,I("Enter two numbers: ").split());cal = Calculator(a,b);return cal
    def D():a=int(I("Enter the number: "));cal = Calculator(a,None);return cal 
    Z=I('Operations available:\n1 - Add\n2 - Subtract\n3 - Multiply\n4 - Divide\n5 - Exponentiation\n6 - Factorial\nEnter the operation index: ')
    if Z.isdigit():
        if Z=='1':P(H,C().add())
        elif Z=='2':P(H,C().sub())
        elif Z=='3':P(H,C().mul())
        elif Z=='4':P(H,C().div())
        elif Z=='5':P(H,C().exp())
        elif Z=='6':P(H,D().fac())
    else:P('Invalid')
    D=I('Do you want to do another calculation? [Y/N]: ')
    if D=='N' or D=='n':break

