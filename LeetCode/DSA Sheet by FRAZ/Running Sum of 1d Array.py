https://leetcode.com/problems/running-sum-of-1d-array/description/

Time Complexity - O(n)
Space Complexity = O(n)
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        new_list = []
        runn_sum = 0
        for i in nums:
            runn_sum +=i
            new_list.append(runn_sum)
        
        return new_list

Best) Approach 2 - InPlace Calculation - Mathematics
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        # time complexity O(n) 
        # space complexity O(1)
        for i in range(1,len(nums)):
            nums[i] = nums[i-1] + nums[i]

        return nums
