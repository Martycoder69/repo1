l=[2,4,3,6,9,1]
for i in l:
    for k in l:
        if i+k==7:
            if i==k:
             continue
            else:
                print(i,k) 