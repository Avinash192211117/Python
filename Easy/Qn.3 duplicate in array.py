Array=[15, 14, 25, 14, 32, 14, 31]
dup_arr=[]
for i in Array:
    if i not in dup_arr:
        dup_arr.append(i)
dup_arr.sort()
print(dup_arr)
