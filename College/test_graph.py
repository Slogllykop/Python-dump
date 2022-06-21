# import numpy as np
# import matplotlib.pyplot as plt


# n=int(input("Enter the number of entries: "))

# heading=input("Enter the heading for the graph: ")

# X_title=input("Enter name of the X Axis: ")
# Y_title=input("Enter name of the Y Axis: ")


# x=np.empty((n,),dtype=float)
# y=np.empty((n,),dtype=float)


# c=0
# while c<n:
#     if c==0:print("Enter 1st entry for x axis:",end = ' ')
#     elif c==1:print("Enter 2nd entry for x axis:",end = ' ')
#     elif c==2:print("Enter 3rd entry for x axis:",end = ' ')
#     else:print("Enter ",c+1,"th entry for x axis:",end = ' ')
#     x[c]=float(input())
#     if c==0:print("Enter 1st entry for y axis:",end = ' ')
#     elif c==1:print("Enter 2nd entry for y axis:",end = ' ')
#     elif c==2:print("Enter 3rd entry for y axis:",end = ' ')
#     else:print("Enter ",c+1,"th entry for y axis:",end = ' ')
#     y[c]=float(input())
#     c+=1


# fig,ax=plt.subplots(figsize=(10,5))
# ax.plot(x,y,marker='o',markerfacecolor='black')
# ax.grid()
# plt.title(heading)
# plt.xlabel(X_title)
# plt.ylabel(Y_title)
# plt.show()
import numpy as N,matplotlib.pyplot as M
P,F,I,Q=print,float,input,'Invalid!'
while True:
    a=I("Enter the number of entries: ")
    if a.isdigit():a=int(a);break
    else:P(Q)
b=I("Enter the heading for the graph: ")
c=I("Enter name of the X Axis: ")
d=I("Enter name of the Y Axis: ")
x=N.empty((a,),dtype=F)
y=N.empty((a,),dtype=F)
i,O,j,k,l=0,' ','Enter ','entry for x axis:','entry for y axis:'
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
e.grid()
e.plot(x,y,marker='o',markerfacecolor='black')
M.title(b)
M.xlabel(c)
M.ylabel(d)
M.show()