def repeat(n):
    arr=[]
    for i in range(n):
        arr.append(int(input("Enter a number : ")))
    x=n-1
    y=0
    for i in range(n-1):
        for j in range(i+1,n):
            if arr[i]==arr[j]:
                if j<x:
                    x=j
                    y=arr[i]
    print(str(y)+ " is the first repeating element and occurs again at index "+str(x))
repeat(int(input("Enter size of list : ")))