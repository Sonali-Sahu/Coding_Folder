https://leetcode.com/problems/running-sum-of-1d-array/description/

Time Complexity - O(n)
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        new_list = []
        runn_sum = 0
        for i in nums:
            runn_sum +=i
            new_list.append(runn_sum)
        
        return new_list
