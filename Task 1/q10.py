def lunh(name):
    change=""
    for letter in name:
        if letter!=' ':
            change += letter
    total = 0
    counter=1
    l=len(change)
    for num in range(l-1,-1,-1):
        if counter%2==0:
            st=int(change[num])*2
            if st>9:
                st-=9
            total+=st
        else:
            total+=int(change[num])
        counter+=1
    if total%10==0:
        return True
    return False

s=input("Enter a credit card number: ")
if lunh(s):
    print("Your credit card number is valid ")
else:
    print("Your credit card number is not valid")