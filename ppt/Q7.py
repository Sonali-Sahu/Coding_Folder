# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the nonzero elements.

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums[:] = list(a for a in nums if a!=0) + list(a for a in nums if a==0)
