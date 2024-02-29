t=int(input("Enter the Limited Time :"))
e=[]
l=[]
for i in range(0,t):
    temp=int(input("Enter the number of guest :"))
    e.append(temp)
for i in range(0,t):
    temp2=int(input("Enter the number of guest :"))
    l.append(temp2)
print("E :",e)
print("L :",l)
n=0
b=[]
res=[]
while(n!=t):
    if(n==0):
        c=e[n]-l[n]
        res.append(c)
        b.append(c)
    elif(n>0):
        temp=b[n-1]+(e[n]-l[n])
        b.append(temp)
        res.append(temp)
    n+=1
print("Res :",res)
print("Maximum number of guest :",max(res))
    
    
