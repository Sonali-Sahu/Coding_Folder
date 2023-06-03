# Given an integer array nums of length n where all the integers of nums are in the range [1, n] and each integer 
# appears **once** or **twice**, return *an array of all the integers that appears **twice***.

# You must write an algorithm that runs in O(n) time and uses only constant extra space.

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        hm = {}
        for i, v in enumerate(nums):
            if v not in hm:
                hm[v] = 1
            else:
                hm[v] += 1
        for key, value in hm.items():
            if value > 1:
                res.append(key)
        return res
