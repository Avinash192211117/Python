total=int(input("Enter the Total user :"))
staff=int(input("Enter the Staff User :"))
if(total<=0 or staff<=0):
    print("Invalid Input...")
else:
    student=((3*total)-(4*staff))//3
    print("Total Number of Student User :",student)
