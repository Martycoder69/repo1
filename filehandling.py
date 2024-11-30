f=open("createdfile.txt","r")
a=f.readlines()
capCount=0
smCount=0
for i in a:
    for j in i:
        if j.isupper():
            capCount+=1
        else:
            smCount+=1
print(capCount)
print(smCount)