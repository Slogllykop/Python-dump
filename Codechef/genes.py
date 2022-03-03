def A(a,b):
    if a=='r' or a=="R" or b=='r' or b=='R':return "R"
    elif a=='b' or a=="B" or b=='b' or b=="B":return "B"
    else:return "G"
B,C=map(str,input().split())
print(A(B,C))