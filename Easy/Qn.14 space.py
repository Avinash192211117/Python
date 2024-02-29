strr=input("Enter the string :")
cap=0
space=0
for i in strr:
    if(i.isupper()):
        cap+=1
    elif(i.isspace()):
        space+=1
print(cap)
print(space)
