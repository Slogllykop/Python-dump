def sum_of_n_natural_number(n):
    if n==1 or n==0:return 1 
    else: return n+sum_of_n_natural_number(n-1)
print(sum_of_n_natural_number(0))