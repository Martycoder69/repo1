Allproducts={"fruit":"apple",
             "fruit":"berry",
             "fruit":"pineapple",
             "fruit":"orange",
             "fruit":"banana",
             "pens":"parker",
             "cleaning":"mop",
             "cleaning":"broom stick"}
ap=Allproducts
x="Y"
while x=="Y"or x=="y":
    print("Welcome to the Shop management system!")
    print("1. Add product")
    print("2. update product")
    print("3. Remove product")
    print("4. View all products")
    print("5. search Product")
    print("6. Exit")
    option=int(input("select an option:"))
    if option==1:
        a=input("enter the name of the product:")
        ac=input("enter the category of the product:")
        ap[a]=ac
        print("the product have benn added!")
    elif option==2:
        u=input("enter the name of the product:")
        uc=input("enter the category of the product:")
        ap[u]=uc
        print("the product have benn updated!")
    elif option==3:
        r=input("enter the name of the product:")
        ap.pop(r)
        print("the product have benn removed!")
    elif option==4:
        print(ap)
    elif option==5:
        s=input("enter the name of the product:")
        if s in ap:
            s=ap[s]
            print(s)
    elif option==6:
        exit   
    else:
        print("Choose any option given above") 
    print("do you want to continue:(Y/N)")
    x=input()