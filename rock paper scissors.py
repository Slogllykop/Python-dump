import random as H
P,N,S,Tr,Fa=print,input,'Rock(r) Paper(p) Scissors(s)',True,False
def A(B,C):
    if B==C:return None
    elif B=='r':
        if C=='p':return Tr
        elif C=='s':return Fa
    elif B=='p':
        if C=='s':return Tr
        elif C=='r':return Fa
    elif B=='s':
        if C=='r':return Tr
        elif C=='p':return Fa
def Z(a):
    if a=='r':return 'Rock'
    elif a=='p':return 'Paper'
    elif a=='s':return 'Scissors'
def X(a):
    if a==1:return 'r'
    elif a==2:return 'p'
    elif a==3:return 's'
while Tr:
    P("Computer's turn:",S,': Computer Chose!');D=H.randint(1,3);E=X(D);F=N(f'Your turn: {S}: ')
    if F=='r' or F=='p' or F=='s':
        P(f"Your choice: {Z(F)}, Computer's choice: {Z(E)}");G=A(E,F)
        if G==None:P('Tie!')
        elif G:P('You Win!')
        else:P('You Lose!')
    else:P('Invalid!')
    I=N('Do you want to play another round? [Y/N]: ')
    if I=='n' or I=='N':break