#Author: Satish Patel
def kth_smallest(a,k):
    return 0

def kth_largest(a,k):
    return 0
    
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    k = int(input())
    print(kth_smallest(a,k))