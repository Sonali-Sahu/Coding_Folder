https://leetcode.com/problems/squares-of-a-sorted-array/description/

# TC = O(n)
# SC = O(n) , as we create an new array
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # create a new array
        new_array = ['_'] * n

        left,right = 0 , n-1

        for i in range(n-1,-1,-1):
            if abs(nums[left]) > abs(nums[right]):
                new_array[i] = nums[left]**2
                left +=1
            else:
                new_array[i] = nums[right]**2 
                right -=1
        return new_array
    
