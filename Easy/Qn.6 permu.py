from itertools import permutations
def permun(num):
    perm=permutations(str(num))
    for i in perm:
        print(i)
num=int(input("Enter the number :"))
permun(num)
