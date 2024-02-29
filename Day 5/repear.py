word=input("Enter the Word :")
a={}
for i in word:
    c=-1
    for j in word:
        if(i==j):
            c+=1
    a[i]=c
for i in a:
    if a[i]>0:
        print(i,"=",a[i])
