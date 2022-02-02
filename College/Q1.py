A=print
B=int(input('Enter base salary: '))
H,T=B/10,B/20
G=B+H+T
P=G/50
N=G-P
A(f'Gross salary: Rs.{G}\nNet salary: Rs. {N}')