def pat1(n):
    for i in range(n):
        for j in range(n-1,i,-1):
            print(" ",end="")
        for k in range(n-i,n+1):
            print("* ",end="")
        print()
    for i in range(n):
        for j in range(i):
            print(" ",end="")
        for k in range(n-i):
            print("* ",end="")
        print()
def pat2(number):
    number
    for i in range(number+1):
        for j in range(i+1):
            print("*",end="")
        for k in range(2*(number-i)-3):
            print(" ",end="")

        print()



num=int(input("Enter a number : "))
pat1(num)