l=[[1,2,3],[4,5,6],[7,8,9]]
for i in range(len(l)-1,-1,-1):
    for j in range(len(l[0])-1,-1,-1):
        print(l[i][j],end=" ")
    print()