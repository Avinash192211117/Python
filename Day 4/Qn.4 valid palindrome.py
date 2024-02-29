s=input("Enter the string :")
str1=""
str2=""
for i in s:
    if(i.isalnum()):
        str1=str1+i.lower()
        str2=i.lower()+str2
if(str1==str2):
    print("Palindrome...")
else:
    print("Not a Palindrome...")
