a = [0]* 100001
a[0] = 1
a[1] = 1
for i in range(2,100001):
    a[i] = a[i-1] + a[i-2]
for _ in range(int(int(input()))):
    n = int(input())
    print(a[n])