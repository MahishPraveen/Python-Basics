units=int(input("enter units consumed"))
if units<=100:
    amt=0
    print(amt)
elif units<=300:
    amt=(units-100)*3
    print(amt)
elif units<=500:
    amt=(units-300)*5
    print(amt)
else:
    amt=1600+(units-500)
    print(amt)
