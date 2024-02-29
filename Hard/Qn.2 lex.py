def findnumber(num):
    return ((n+1)*(n+2)*(n+3)*(n+4)/24)
n=int(input("Enter the length :"))
if(n<=0):
    print("Invalid Length :")
else:
    print("Count :",findnumber(n))
