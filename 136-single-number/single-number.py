class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        m = defaultdict(int)
        for val in nums:
            m[val] += 1
        
        for key, val in m.items():
            if val == 1:
                return key
        
        return -1