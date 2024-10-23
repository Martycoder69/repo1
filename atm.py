a=1000
e=a
x="Y"
while x=="Y"or x=="y":
    print("1. check balance")
    print("2. withdraw cash")
    print("3. deposit cash")
    print("4. exit")
    choice=int(input("enter your choice:"))
    if choice==1:
        print("checking balance...")
        print(e)
    elif choice==2:
        b=int(input("enter the amount you want to withdraw:"))
        e=e-b
        print("the amount left on your account is ")
        print(e)
    elif choice==3:
        d=int(input("enter the amount of cash you want deposit:"))
        e=e+d
        print("the amount left on your account is ")
        print(e)
    elif choice==4:
        exit()
    else:
        print("wrong choice!")
    print("do you want to continue:(Y/N)")
    x=input()
    