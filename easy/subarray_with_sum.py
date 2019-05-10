def subArraySum(arr, n, k):
	curr_sum = arr[0] 
	start = 0
	i = 1
	while i <= n: 
		while curr_sum > k and start < i-1:		
			curr_sum = curr_sum - arr[start] 
			start += 1
		if curr_sum == k:			
			print ("%d %d"%(start+1, i)) 
			return 1
		if i < n: 
			curr_sum = curr_sum + arr[i] 
		i += 1
	print (-1) 
	return 0
for _ in range(int(input())):
    n, k = map(int,input().split())
    a = list(map(int, input().split()))
    subArraySum(a,n,k)