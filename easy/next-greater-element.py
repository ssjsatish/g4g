def next_greater(a,n):
    s = []
    ans = [-1 for i in range(n)]
    for i in range(n-1, -1, -1):
        while s and s[-1]<=a[i]:
            s.pop()
        if len(s)>0:
            ans[i] = s[-1]
        s.append(a[i])
    return ans

a   = [    9, 2, 3, 5, 1,  6,   2 ]
# ans = [ -1, 3, 5, 6, 6, -1, -1  ]
print(*(next_greater(a,len(a))))
print("Its Done");