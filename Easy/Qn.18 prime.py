def prime(a):
    for x in range (2,a):
        if (a%x== 0):
            return False
            break
    return True
a = int(input("Enter starting value :"))
print(prime(a))
