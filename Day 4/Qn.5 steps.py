str1=input("Enter the Numbers (with space):")
n=str1.split()
nums=[int(i)for i in n]
i=0
c=0
n=len(nums)
print(n)
while(i<n):
    d=i+nums[i]
    print("Travel :",nums[i])
    c=1
    if(d>=n):
        i=n
    i=d
print("count :",c)
