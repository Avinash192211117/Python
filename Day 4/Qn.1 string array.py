n=int(input("Enter the length :"))
lisst=[]
for i in range(1,n+1):
    if(i%3==0 and i%5==0):
        lisst.append("FizzBuzz")
    elif(i%3==0):
        lisst.append("Fizz")
    elif(i%5==0):
        lisst.append("Buzz")
    else:
        lisst.append(str(i))
print(lisst)
