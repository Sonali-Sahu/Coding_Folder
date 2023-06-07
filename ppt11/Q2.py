# A peak element is an element that is strictly greater than its neighbors.

# Given a **0-indexed** integer array `nums`, find a peak element, and return its index. 
# If the array contains multiple peaks, return the index to **any of the peaks**.


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        nums_len = len(nums)
        left,right = 0, nums_len-1
        while left<right:
            middle = (left+right) >> 1
            if nums[middle]<nums[middle+1]:
                left = middle + 1
            else:
                right = middle
        return left
