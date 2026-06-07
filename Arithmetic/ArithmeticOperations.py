a=int(input("Enter the value of a"))
b=int(input("Enter the value of b"))
choice=input("Enter the choice +-*///**%")
if choice=="+":
    result=a+b
    print("sum=",result)
elif choice="-":
    result=a-b
    print(result)
elif choice="*":
    result=a*b
    print(result)
elif choice="/":
    result=a/b
    print(result)
elif choice ="//":
    result=a//b
    print(result)
elif choice ="**":
    result=a**b
    print(result)
elif choice ="%":
    result=a%b
    print(result)
else:
    print("Invalid Operator")
