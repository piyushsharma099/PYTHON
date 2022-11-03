l=[1,'hello',2,'python']
for i in range(len(l)):
    if(type(l[i])==str):
        l[i]=" "
print(l)