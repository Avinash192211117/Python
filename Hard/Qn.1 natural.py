n=int(input("Enter how many natural :"))
sumofsq=0
summ=0
if(n<=0):
    print("Invalid Input...")
else:
    for i in range(1,n+1):
        sumofsq+=i**2
        summ+=i
    sqofsum=summ**2
    print("Sum of Square :",sumofsq)
    print("Square of Sum :",sqofsum)
    print("Difference :",sqofsum-sumofsq)
