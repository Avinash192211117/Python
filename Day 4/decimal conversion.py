num=input("Enter the binary number :")
flag=0
for i in range(0,len(num)):
    if(num[i]!='0' and num[i]!='1'):
        flag=1
        break
if(flag==0):
    dec=int(num,2)
    octal=oct(dec)
    hexa=hex(dec)
    print("Decimal Value :",dec)
    print("Octal Value :",octal)
    print("Hexa value :",hexa)
else:
    print("Invalid binary number")
