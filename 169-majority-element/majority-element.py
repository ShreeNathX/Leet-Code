class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        m = defaultdict(int)

        for val in nums:
            m[val] += 1
        
        c = len(nums) // 2

        for key, val in m.items():
            if val > c:
                return key
        return -1
        
        