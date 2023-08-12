1. time complexity = O(n^2)
using for loop:-

Solution 1 :- 
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i in range(len(nums)):
            for j in range(i,len(nums)):
                if nums[i] + nums[j] == target and  i!=j:
                    return [i,j]


2. 
                
