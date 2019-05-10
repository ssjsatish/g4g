def next_greater(a):
    s = []
    element = 0
    next = 0
    s.append(a[0])
    for i in range(1, len(a)):
        next = a[i]
        if len(s) > 0:
            element = s.pop()
            while element < next:
                print(next, end = ' ')
                if len(s) == 0:
                    break
                element = s.pop()
            if element > next:
                s.append(element)
        s.append(next)
    while len(s) > 0:
        element = s.pop()
        next = next - 1
        print(-1, end =' ')
    print()

a   = [    9, 2, 3, 5, 1,  6,   2 ]
# ans = [ -1, 3, 5, 6, 6, -1, -1  ]
next_greater(a)