a=int(input("enter the number:"))
b=int(input("enter the second number:"))
def Addition(a,b):
    print(a+b)
def Subtraction(a,b):
    print(a-b)
def Division(a,b):
    c=a/b
    return c
def Multiplication(a,b):
    d=a*b
    return d
print("1. Addition")
print("2. Subtraction")
print("3. Division")
print("4. Multiplication")
choice=int(input("enter your choice:"))
if choice==1:
        Addition(a,b)
elif choice==2:
        Subtraction(a,b)
elif choice==3:
        print(Division(a,b))
elif choice==4:
        print(Multiplication(a,b))