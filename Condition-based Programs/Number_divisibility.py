n=int(input("Enter a number"))
if n%5==0 and n%7==0:
    print(n,"is divisible by 5 and 7")
elif n%5==0 or n%7==0:
    print(n,"is either divisible by 5 and 7")
else:
    print(n,"is not divisible by both")
