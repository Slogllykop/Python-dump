A="Dear <NAME>,\n\tGreetings from XYZ Company, I'm happy that you got selected\nYou are selected!\nDate: <DATE>"
B=input
C=B("What's your name?\n")
D=B("What's the date today?\n")
A=A.replace('<NAME>',C)
A=A.replace('<DATE>',D)
print(A)