strr=input("Enter the string :")
vowels=["A","a","E","e","I","i","O","o","U","u"]
v=0
print("Vowels :")
for i in range(0,len(strr)):
    if(strr[i] in vowels):
        v=v+1
print(v)
    
