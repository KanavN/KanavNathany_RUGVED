def anagram(m,n):
    l1=len(m)
    l2=len(n)
    check="abcdefghijklmnopqrstuvwxyz"
    for letter in check:
        count1=0
        count2=0
        for letter2 in m:
            if letter==letter2:
                count1+=1
        for letter3 in n:
            if letter==letter3:
                count2+=1
        if count1!=count2:
            return False
    return True
a=input("enter first string: ")
b=input("enter second string: ")
if anagram(a,b):
    print("They are anagrams")
else:
    print("They are not anagrams")

