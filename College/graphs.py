import numpy as N,matplotlib.pyplot as M
P,F,I,Q,j=print,float,input,'Invalid!','Enter '
b,c,d,g,h=I(f"{j}the heading for the graph: "),I(f"{j}name of the X Axis: "),I(f"{j}name of the Y Axis: "),I(f'{j}your Name and Surname: '),I(f'{j}your Roll Number: ')
while True:
    a=I("Enter the number of entries: ")
    if a.isdigit():a=int(a);break
    else:P(Q)
x=N.empty((a,),dtype=F)
y=N.empty((a,),dtype=F)
i,O,k,l=0,' ','entry for x axis:','entry for y axis:'
while i<a:
    while True:
        if i==0:P(f'{j}1st {k}',end=O)
        elif i==1:P(f'{j}2nd {k}',end=O)
        elif i==2:P(f'{j}3rd {k}',end=O)
        else:P(f'{j}{i+1}th {k}',end=O)
        m=I()
        if m.replace('.','',1).isdigit():x[i]=F(m);break
        elif m.isdigit():x[i]=F(m);break
        else:P(Q)
    while True:
        if i==0:P(f'{j}1st {l}',end=O)
        elif i==1:P(f'{j}2nd {l}',end=O)
        elif i==2:P(f'{j}3rd {l}',end=O)
        else:P(f'{j}{i+1}th {l}',end=O)
        n=I()
        if n.replace('.','',1).isdigit():y[i]=F(n);break
        elif n.isdigit():y[i]=F(n);break
        else:P(Q)
    i+=1
f,e=M.subplots(figsize=(10,5))
e.grid();e.plot(x,y,marker='o',markerfacecolor='black')
M.text(-0.05, 1.1, f'Roll no: {h} - {g}',horizontalalignment='left',verticalalignment='center',transform=e.transAxes);M.title(b);M.xlabel(c);M.ylabel(d);M.show()