https://leetcode.com/problems/move-zeroes/description/

# took hint , Try again


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0 and nums[j] == 0:
                # j index will have number and  0 will be pushed back to i index
                nums[i],nums[j] = nums[j],nums[i]

            if nums[j] != 0 :
                # increase j value if the nums[j] ! = 0 
                j+= 1
        
