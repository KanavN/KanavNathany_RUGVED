def triple_and(a,b,c):
    if a =='True' and b == 'True' and c == 'True':
        return True
    else:
        return False
x=input("enter True or False: ")
y=input("enter True or False: ")
z=input("enter True or False: ")
print(triple_and(x,y,z))
