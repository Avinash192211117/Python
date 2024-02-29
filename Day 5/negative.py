def compo(arr):
    res=[]
    for i in arr:
        if(i<0):
            res.append(i)
    return res
arr=[16,-18,27,-16,23,-21,19]
print(compo(arr))
print("Count :",len(compo(arr)))
