def itna(a):
    if len(a)>9:new_itna=f'{a[:7]}..';return new_itna
    elif len(a)<9:name_length=len(a);return f"{a}{' '*(9-name_length)}"
    else: return a
def itqu(a):
    if len(a)>4:return 0 
    for i in range(1,5):
        if len(a)==i:return f"{' '*(6-(i-1))}{int(a)}{' '*6}"
def itpr(a):
    if len(a)>5:return 0
    for i in range(1,6):
        if len(a)==i:return f"{' '*(10-i)}{int(a)}"
print('\nEnter the information seperated with a space, for eg.\nRice_cake 10 20')
counter,item_name,item_quantity,item_price=[],[],[],[]
while True:
    print(f"\n{'*'*18}Bill{'*'*18}\nItem name    Item Quantity    Item Price\n{'*'*40}")
    item=list(map(str,input().split()))
    if len(item[1])<5 and len(item[2])<6:
        ppi=int(item[1])*int(item[2]);counter.append(ppi)
    else:counter.append(0)
    item_name.append(itna(item[0]));item_quantity.append(itqu(item[1]));item_price.append(str(itpr(item[2])))
    A=input('\nDo you want to add another item [Y/N]: ')
    if A=='n' or A=='N':
        print(f"\n{'*'*18}Bill{'*'*18}\nItem name    Item Quantity    Item Price")
        print('*'*40)
        for j in range(len(item_name)):
            if item_quantity[j]==0:
                if item_price[j]=='0':print(f"{item_name[j]}    Out of Stock!    Expensive!")
                else:print(f"{item_name[j]}    Out of Stock!    {item_price[j]}")
            elif item_price[j]=='0':
                if item_quantity[j]==0:print(f"{item_name[j]}    Out of Stock!    {' '*9}0")
                else:print(f"{item_name[j]}    {item_quantity[j]}    Expensive!")
            else:print(f"{item_name[j]}    {item_quantity[j]}    {item_price[j]}")
        print(f"{'*'*40}\nTotal amount to be paid: Rs.{sum(counter)}/-\n{'*'*40}")
        break