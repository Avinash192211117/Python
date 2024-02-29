def merging(s1,s2):
    res=""
    for i in range(max(len(s1),len(s2))):
        if(i<len(s1)):
            res+=s1[i]
        if(i<len(s2)):
            res+=s2[i]
    return res
w1=input("Enter the first word :")
w2=input("Enter the second Words :")
print("Output String :",merging(w1,w2))
