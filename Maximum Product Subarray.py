# link :- https://leetcode.com/problems/maximum-product-subarray/description/

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        max_till_now = 1
        min_till_now = 1
        for i in nums:
            exp = (max_till_now*i,min_till_now*i,i)
            max_till_now,min_till_now = max(exp),min(exp)
            res = max(max_till_now,res)
        return res
