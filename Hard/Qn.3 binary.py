bin1=input("Enter the First Binary :")
bin2=input("Enter the Second BInary :")
if(bin1[0]=='0'and len(bin1)!=1):
    bin1=bin1.lstrip('0')
if(bin2[0]=='0'):
    bin2=bin2.lstrip('0')
num1=int(bin1,2)
num2=int(bin2,2)
summ=num1+num2
print("First Binary :",bin1)
print("Second Binary :",bin2)
print("Sum of Binary :",bin(summ)[2:])
