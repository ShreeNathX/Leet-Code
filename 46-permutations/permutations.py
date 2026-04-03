class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = [False] * len(nums)

        def backtrack(path):
            if len(path) == len(nums):
                res.append(path[:])
                return
            for _ in range(len(nums)):
                if not used[_]:
                    used[_] = True
                    path.append(nums[_])
                    backtrack(path)
                    path.pop()
                    used[_] = False
        backtrack([])
        return res