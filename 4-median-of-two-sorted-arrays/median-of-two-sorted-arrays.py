class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        nums.sort()
        n = len(nums)
        if n % 2 == 0:
            median1 = nums[n//2]
            median2 = nums[n//2 - 1]
            median  = (median1 + median2) / 2
        else:
            median = nums[n//2]
        return median