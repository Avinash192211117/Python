def climb(n):
    if n<2:
        return 1
    else:
        return (climb(n-1)+climb(n-2))
num=int(input("Enter the steps :"))
print(climb(num))
