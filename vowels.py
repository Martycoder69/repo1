p=input("enter password")
if len(p)>8:
    for i in range(len(p)):
        if p[i]==["A-Z"]or ["a-z"] or ["0-9"]:
print("valid password")
        else:
            print("invalid password")
else:
    print("enter min 8 char")
    