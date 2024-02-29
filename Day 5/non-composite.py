def compo(arr):
    res=[]
    for i in arr:
        summ=0
        for j in range(2,i):
            if(i%j==0):
                res.append(i)
                break
    return res
arr=[26,28,47,26,43,51,29]
comp=compo(arr)
for i in arr:
    if i not in comp:
        print(i)
