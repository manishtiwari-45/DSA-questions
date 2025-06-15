class Solution:
    def maximumSumSubarray(self, arr, k):
        currSum = 0
        maxSum = 0
        i = 0
        j = 0
        
        while j < len(arr):
            currSum += arr[j]
            
            if j - i + 1 < k:
                j += 1
            elif j - i + 1 == k:
                maxSum = max(maxSum, currSum)
                currSum -= arr[i]
                i += 1
                j += 1
                
        return maxSum
