total=eval(input("Enter Total user :"))
staff=eval(input("Enter Staff Users :"))
if(total<=0 or staff<=0):
    print("Invalid....")
else:
    student=(3*total-4*staff)//3
    print(student)
