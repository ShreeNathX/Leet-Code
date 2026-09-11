class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        arr = []
        for i in range(len(nums)):
            curr = nums[i]
            count = 0

            for j in range(len(nums)):
                if nums[j] < curr:
                    count += 1
            arr.append(count)
        return arr