class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        for _ in range(1, len(nums)+2):
            if _ not in nums_set:
                return _