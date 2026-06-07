sales = int(input("Enter sales"))
if sales>=50000:
    comm=sales*10/100
    print("sales=",sales,"comm=",comm)
elif sales>=30000:
    comm=sales*8/100
    print("sales=",sales,"comm=",comm)
elif sales>=10000:
    comm=sales*5/100
    print("sales=",sales,"comm=",comm)
else:
    comm=sales*1/100
    print("sales=",sales,"comm=",comm)
