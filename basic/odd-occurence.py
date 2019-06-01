def odd_occurence(a,n):
    a.sort()
    print(a)
    count = 1
    temp = a[0]
    for i in range(1, n):
        if a[i] == a[i-1]:
            count +=1
        else:
            if count%2==1:
                return a[i]
            else:
                count=0
    return 0
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    print(odd_occurence(a,n))


# a = [1,1,2,3,3]