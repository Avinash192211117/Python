strr=input("Enter the string :")
vowels=["A","a","E","e","I","i","O","o","U","u"]
out=""
for i in strr:
    if i not in vowels:
        out=out+i
print("After Removing Vowels:")
print(out)
