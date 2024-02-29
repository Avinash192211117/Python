har=input("Enter the character")
n=int(input("enter the row:"))
if(n<=0):
    print("Invalid Input.....")
else:
    for i in range(0,n+1):
        for j in range(0,i):
            print(har,end=" ")
        print("\n")
