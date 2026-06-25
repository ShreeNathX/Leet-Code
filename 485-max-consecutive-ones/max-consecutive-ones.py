class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = cons = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
                cons = max(count, cons)
            else:
                count = 0
        return cons