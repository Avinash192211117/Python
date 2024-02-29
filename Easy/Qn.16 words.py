strr=input("Enter the String :")
word=0
for i in strr:
    if(i.isspace()):
        word+=1
print(f"Words :{word+1}")
