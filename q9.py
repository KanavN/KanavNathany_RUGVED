def encrypt(num,name):
    final=""
    low="abcdefhgijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    upp=low.upper()
    for letter in name:
        if letter.islower():
            count=low.index(letter)
            final+=low[count+(num%26)]
        elif letter.isupper():
            count=upp.index(letter)
            final+=upp[count+(num%26)]
        else:
            final+=letter
    print(final)
number=int(input("Enter a number: "))
name1=input("Enter a string: ")
encrypt(number,name1)