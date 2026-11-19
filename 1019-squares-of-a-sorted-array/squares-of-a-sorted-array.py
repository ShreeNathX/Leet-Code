class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        n = len(nums)

        i, j, k = 0, n-1, n-1
        res = [0]*n

        while i <= j:
            if abs(nums[i]) > abs(nums[j]):
                res[k] = nums[i] * nums[i]
                i +=1
            else:
                res[k] = nums[j] * nums[j]
                j-=1
            k-=1
        return res