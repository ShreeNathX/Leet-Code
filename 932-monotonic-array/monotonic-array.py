class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        # increasing = True
        # decreasing = True

        # for i in range(1, len(nums)):
        #     if nums[i] < nums[i-1]:
        #         increasing = False
        #     elif nums[i] > nums[i-1]:
        #         decreasing = False
        
        # return increasing or decreasing
        #return nums == sorted(nums) or nums == sorted(nums, reverse = True)
        return all(nums[i] <= nums[i+1] for i in range(len(nums)-1)) or all(nums[i] >= nums[i+1] for i in range(len(nums)-1)) 