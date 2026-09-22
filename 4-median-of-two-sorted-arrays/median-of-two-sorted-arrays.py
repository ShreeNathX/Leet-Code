class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        nums = nums1 + nums2
        nums.sort()
        n = len(nums)

        if n % 2 == 0:
            median = (nums[n//2] + nums[n//2 -1])/2
        else:
            median = nums[n//2]
        
        return median