def knapsack(W, wt, v,n):
    dp = [[]]
    for col in range(W+1):
        dp[0][col] = 0
    for row in range(1,n+1):
        dp[row][0] = 0
    for i in range(0,n+1):
        for w in range(0,W+1):
            if i==0 or w==0: 
                dp[i][w] = 0
            elif wt[i-1] <= w: 
                dp[i][w] = max(v[i-1] + dp[i-1][w-wt[i-1]],  dp[i-1][w]) 
            else: 
                dp[i][w] = dp[i-1][w]            
    return dp[n][W]
    
for _ in range(int(input())):
    n = int(input())
    W = int(input())
    wt = list(map(int, input().split()))
    v = list(map(int, input().split()))
    print(knapsack(W, wt,v,n))
