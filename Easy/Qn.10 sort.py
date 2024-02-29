strr=input("Enter the string :")
v=[]
for i in strr:
    v.append(i)
v.sort()
v.reverse()
sort="".join(v)
print(sort)
