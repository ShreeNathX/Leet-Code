class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        TotalSum = sum(nums)
        LeftSum = 0
        for i in range(len(nums)):
            RightSum = TotalSum - LeftSum - nums[i]
            if RightSum == LeftSum:
                return i
            LeftSum += nums[i]
        return -1