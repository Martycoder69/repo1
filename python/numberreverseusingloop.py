a=int(input("enter a number:"))
b=0
while(a>0):
    i=a%10
    b=b*10+i
    a=a//10
print(b)