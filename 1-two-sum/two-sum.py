class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # Using Hasmap
        m = defaultdict(int)
        
        for i, val in enumerate(nums):
            temp = target - val

            if temp in m:
                return [m[temp], i]
            
            m[val] = i