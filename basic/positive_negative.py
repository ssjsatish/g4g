for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    pos = []
    neg = []
    for i in a:
        if i<0:
            neg.append(i)
        else:
            pos.append(i)
    i = 0
    minL = min(len(pos), len(neg))
    while i< minL:
        print(pos[i],neg[i],end=' ')
        i += 1
    if len(pos)>len(neg):
        for j in range(i,len(pos)):
            print(pos[i], end=' ')
    else:
        for j in range(i, len(neg)):
            print(neg[i],end=' ')
    print()
    