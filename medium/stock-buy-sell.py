#Author: Satish Patel

for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    local_minima = 0
    local_maxima = 0
    count = 0
    counter = 0
    while counter < n-1:
        flag = 0
        while counter < n-1 and a[counter] > a[counter+1]:
            local_minima = counter + 1
            counter +=1
        while counter < n-1 and a[counter] < a[counter+1]:
            local_maxima = counter + 1
            counter +=1
            flag = 1
        if flag == 1:
            print("("+local_minima+" "+ local_maxima+")", end = " ")
            count +=1
        if counter == n-1:
            break
    if count == 0:
        print("No Profit", end=" ")
    print()