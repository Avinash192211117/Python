x=int(input("Enter the number:"))
y=[]
print("The factors of",x,"are:")
for i in range(1, x + 1):
    if x % i == 0:
        y.append(i)
print(y)
print("Number of factors:", len(y))
n=int(input("Enter N value:"))
if n>len(y):
    print("Invalid")
else:
    print("First",n,"factors")
    for i in range(0,n):
        print(y[i],end=' ')
