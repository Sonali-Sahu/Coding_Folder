https://leetcode.com/problems/majority-element/description/

## time complexity = O(n) , Space Complexity = O(1)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num_set = set(nums)
        n = len(nums)
        for i in num_set:
            if nums.count(i) > n//2:
                return i
            
        return -1


# Could you solve the problem in linear time and in O(1) space?

