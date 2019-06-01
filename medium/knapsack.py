def knapsack(W, wt, v,n):
    #B = [[0 for i in range(W+1)] for j in range(n)]
    dp = [[]]
    for col in range(W+1):
        dp[0][col] = 0
    for row in range(1,n+1):
        dp[row][0] = 0
    for i in range(n+1):
        for w in range(W+1):
            if i==0 or w==0: 
                K[i][w] = 0
            elif wt[i-1] <= w: 
                dp[i][w] = max(v[i-1] + dp[i-1][w-wt[i-1]],  dp[i-1][w]) 
            else: 
                dp[i][w] = dp[i-1][w] 

            '''
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif wt[i-1] <= j:
                if v[i] + dp[i-1][w-W[i]] > dp[i-1][w]:
                    dp[i][w] = v[i] + dp[i-1][w-W[i]]
                else:
                    dp[i][w] = v[i-1][w]
            else:
                dp[i][w] = v[i-1][w]'''
    return dp[n][W]

'''
for _ in range(int(input())):
    n = int(input())
    w = int(input())
    vals = list(map,int(input().split()))
    wts = list(map,int(input().split()))
    dp = [[0] * (w + 1) for _ in range(n)]
    
    for i in range(w + 1):
        dp[0][i] = vals[0] if wts[0] <= i else 0
    
    for i in range(1, n):
        for j in range(1, w + 1):
            if j<wts[i]:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-wts[i]] + vals[i])
    
    print(dp[n-1][w])
    '''



for _ in range(int(input())):
    n = int(input())
    W = int(input())
    wt = list(map(int, input().split()))
    v = list(map(int, input().split()))
    print(knapsack(W, wt,v,n))
