n=int(input("Enter the number of elements :- "))
l=[]
sum=0
for i in range(n):
    x=int(input())
    l.append(x)
for i in range(n):
    sum=sum+l[i]
    avg=sum/n
print("Sum is ",sum)
print("Average is ",avg)