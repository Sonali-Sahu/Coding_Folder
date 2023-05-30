# Q1. Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        leng = len(nums)
        for i in range(leng):
            for j in range(leng):
                #print(i,j)
                if nums[i]+nums[j] == target and i != j:
                    return [i,j]
