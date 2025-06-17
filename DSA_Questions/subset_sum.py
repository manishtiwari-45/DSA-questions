class Solution:
    def isSubsetSum (self, arr, sum):
        # code here 
        n = len(arr)
        dp = [[False  for _ in range(sum+1)] for _ in range(n + 1)]
        for i in range(n + 1):
            dp[i][0] = True 
        
        for i in range(1,len(arr)+1):
            for j in range(1,sum+1):
                if arr[i-1] <= j:
                    dp[i][j] = dp[i-1][j-arr[i-1]] or dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        
        return dp[len(arr)][sum]
                    
        
        
