import random as H
A,I,M,R,P='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*(),./?0123456789',int,input,range,print
while True:
    B,C=M('Enter how many number of passwords to generate: '),M('Enter the length of the passwords: ')
    if B.isdigit():
        for i in R(I(B)):
            D=''
            for a in R(I(C)):D+=H.choice(A)
            P(D)
    else:P('Invalid')
    E=M('Do you want to generate another set of passwords? [Y/N]: ')
    if E=='N' or E=='n':break