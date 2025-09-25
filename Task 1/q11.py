def grade(s):
    word=1
    digit=0
    sentence=0
    for letter in s:
        if letter.isalpha():
            digit+=1
        elif letter.isspace():
            word+=1
        elif letter=='.' or letter=='?' or letter=='!':
            sentence+=1
    l=digit/word*100
    s=sentence/word*100
    index=(0.0588*l)-(0.296*s)-15.8
    print(index)
name=input("Enter a sentence : ")
grade(name)



