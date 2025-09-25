def hill(num):
    l=len(str(num))
    max=0
    s=str(num)
    for letter in s:
        if int(letter)>max:
            max=int(letter)
    if s.index(str(max))==0 or s.index(str(max))==l-1:
        return False
    ref=s.index(str(max))
    for i in range(0,ref):
        if int(s[i])>int(s[i+1]):
            return False
    for i in range(ref,l-1):
        if int(s[i])<int(s[i+1]):
            return False
    return True
number=int(input("enter the number: "))
final=hill(number)
if final:
    print("Hill number")
else:
    print("Not a hill number")