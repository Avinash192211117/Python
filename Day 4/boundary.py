def printBoundary(a, m, n):
    for i in range(m):
        for j in range(n):
            if (i == 0):
                print(a[i][j],end="")
            elif (i==m-1):
                print(a[i][j],end="")
            elif (j==0):
                print(a[i][j],end="")
            elif (j==n-1):
                print(a[i][j],end="")
a = [[1, 2, 3, 4], [5, 6, 7, 8],
         [1, 2, 3, 4], [5, 6, 7, 8]]
printBoundary(a,4,4)
