class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        currSum , maxSum = 0, -inf

        for val in nums:
            currSum += val
            maxSum = max(currSum, maxSum)

            if currSum < 0:
                currSum = 0
        return maxSum
            
        