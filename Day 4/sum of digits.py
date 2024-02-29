def sumofdigits(num):
    summ=0
    while(num>0):
        rem=num%10
        summ+=rem
        num//=10
    return summ
num=int(input("Enter the number:"))
summ=sumofdigits(num)
n=str(summ)
while(len(n)!=1):
    num=summ
    summ=sumofdigits(num)
    n=str(summ)
print("Sum of Digits :",summ)
