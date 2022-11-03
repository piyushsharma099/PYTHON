n=int(input("Enter the elements in the list :- "))
# a=list(map(int,input("Enter the number ").split()))[:n]
# print(a)
l=[]
for i in range(n):
    x=int(input())
    l.append(x)
e=int(input("Enter the elements to be searched :- "))
if(e in l):
    print("Element Found")
else:
    print("Element not Found")