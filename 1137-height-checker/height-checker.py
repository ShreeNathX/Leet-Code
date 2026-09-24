class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        nums = sorted(heights)
        cnt = 0
        for i in range(len(nums)):
            if heights[i] != nums[i]:
                cnt += 1
        
        return cnt