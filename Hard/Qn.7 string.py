s1=input("Enter the String 1 :")
s2=input("Enter the String 2 :")
str3=[]
str1=s1.split()
str2=s2.split()
for i in str1:
    for j in str2:
        if(i in j):
            str3.append(i)
print(str3)
print("Output...")
for i in str1:
    if i not in str3:
        print(i)
for i in str2:
    if i not in str3:
        print(i)
