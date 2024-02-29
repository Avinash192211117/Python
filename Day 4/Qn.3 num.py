str1=input("Enter the Numbers (with space):")
n=str1.split()
nums=[int(i)for i in n]
count=[]
for i in range(0,len(nums)):
    c=0
    for j in range(0,len(nums)):
        if(nums[i]>nums[j] and i!=j):
            c+=1
    count.append(c)
print("Given Array :",nums)
print("Count Array :",count)

