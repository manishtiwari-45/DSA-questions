class Solution:
    def knapsack(self, W, val, wt):
        n = len(val)
        self.dp = [[-1 for _ in range(W + 1)] for _ in range(n + 1)]
        return self.helper(W, val, wt, n)
    
    def helper(self, W, val, wt, n):
        if n == 0 or W == 0:
            return 0
        
        if self.dp[n][W] != -1:
            return self.dp[n][W]
        
        if wt[n - 1] <= W:
            include = val[n - 1] + self.helper(W - wt[n - 1], val, wt, n - 1)
            exclude = self.helper(W, val, wt, n - 1)
            self.dp[n][W] = max(include, exclude)
        else:
            self.dp[n][W] = self.helper(W, val, wt, n - 1)
        
        return self.dp[n][W]
