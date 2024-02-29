def season(mon,day):
    if(mon=='Dec' and day>=21 or mon=='Jan' or mon=='Feb' or mon=='Mar' and day<20):
        print("Winter....")
    elif(mon=='Mar' and day>=20 or mon=='Apr' or mon=='May' or mon=='Jun' and day<21):
        print("Summer....")
    elif(mon=='Jun' and day>=21 or mon=='Jul' or mon=='Aug' or mon=='Sep' and day<22):
        print("Spring....")
    elif(mon=='Sep' and day>=22 or mon=='Oct' or mon=='Nov' or mon=='Dec' and day<21):
        print("Fall...")
    else:
        print("Invalid Date....")
m=input("Enter month :")
date=int(input("Enter the date :"))
mon=m[:3].capitalize()
season(mon,date)
