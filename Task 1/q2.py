name=input("enter a word : ")
counter="abcdefghijklmnopqrstuvwxyz"
final=""
for letter in counter:
    count=0
    for letter2 in name:
        if letter==letter2:
            final=final+letter
            count=count+1

    if count>=1:
         print(letter+" occurs "+str(count)+" times")
print(final)

