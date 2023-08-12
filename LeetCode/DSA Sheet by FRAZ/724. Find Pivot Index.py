https://leetcode.com/problems/find-pivot-index/description/

# Approach - List Comprehension - Time Complexity = O(n), Space Complexity = O(1)
# High Runtime as Sum is used in each loop 2 times
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n =len(nums)
        for i in range(n):
            if sum(nums[:i]) == sum(nums[i+1:]):
                return i
        return -1

  
# Better Approach :- More Mathematical (+/-) than Using Sum So many Time in each loop
# Time Complexity = O(n), Space Complexity = O(1)

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum,right_sum = 0,sum(nums)
        for i, ele in enumerate(nums):
            right_sum -= ele
            if left_sum == right_sum:
                return i
            left_sum += ele
        return -1
            
