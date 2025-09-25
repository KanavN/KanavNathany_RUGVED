n=int(input("Enter size of list : "))
arr=[]
for i in range(n):
    arrr=[]
    for j in range(n):
        arrr.append(int(input("Enter a number : ")))
    arr.append(arrr)
for i in range(n):
    for j in range(i+1,n):
        temp=arr[i][j]
        arr[i][j]=arr[j][i]
        arr[j][i]=temp
for r in arr:
    r.reverse()
for r in range(n):
    for c in range(n):
        print(arr[r][c],end=" ")
    print()


