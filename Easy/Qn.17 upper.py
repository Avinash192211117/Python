strr=input("Enter the String :")
words=strr.split()
str2=""
for word in words:
    new_word=word.capitalize()
    print(new_word[0],end="")
    str2=str2+" "+new_word
print(str2)
