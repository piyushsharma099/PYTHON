n=int(input("Enter the number of elements :- "))
l=[]
l1=[]
l2=[]
print("Enter the elements ")
for i in range(n):
    x=int(input())
    l.append(x)
for i in l:
    if(i not in l1):
        l1.append(i)
    else:
        l2.append(i)
print("unique elements",l1)
print("Repeated elements",l2)