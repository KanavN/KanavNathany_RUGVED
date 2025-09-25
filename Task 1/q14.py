def repeat(n):
    arr=[]
    for i in range(n):
        arr.append(int(input("Enter a number : ")))
    flag=0
    y=0
    for i in range(n-1):
        for j in range(i+1,n):
            if arr[i]==arr[j]:
                y=arr[i]
                flag=1
                break
        if flag==1:
            break
    print(str(y)+ " is the first repeating element ")
repeat(int(input("Enter size of list : ")))