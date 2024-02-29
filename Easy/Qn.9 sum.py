def summation(num):
    summ=0
    while(num!=0):
        rev=num%10
        summ=summ+rev
        num=num//10
    return summ
num=eval(input("Enter the number :"))
summ=summation(num)
n=str(summ)
while(len(n)!=1):
    num=summ
    summ=summation(num)
    n=str(summ)
print(summ)
    

