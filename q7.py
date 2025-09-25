n=int(input("Enter a number: "))
f1=0
f2=1
print(f1)
print(f2)
n-=2
f3=1
while n>0:
    f3=f1+f2
    f1=f2
    f2=f3
    print(f3)
    n-=1