l=["apple","orange","bannana","berry","apple"]
el=[]
for i in l:
    if i in el:
            print(f"list has a duplocate value:{i}")
    else:
        el.append(i)