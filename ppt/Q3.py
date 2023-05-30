# Q3.** Given a sorted array of distinct integers and a target value, return the index if the target is found.
# If not, return the index where it would be if it were inserted in order.

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        i = 0
        for i in range(len(nums)):
            if nums[i]==target or target < nums[i]:
                return i
        return i + 1
