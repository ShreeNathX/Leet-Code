class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        dic = defaultdict(int)

        for idx, val in enumerate(nums):
            temp = target - val

            if temp in dic:
                return [dic[temp], idx]
            
            dic[val] = idx