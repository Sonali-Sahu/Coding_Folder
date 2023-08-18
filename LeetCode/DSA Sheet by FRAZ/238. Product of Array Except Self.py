https://leetcode.com/problems/product-of-array-except-self/description/

# TC = O(n)
# SC = O(n)
# 2 pointer
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        new_sol = [1]*length
        pre,post = 1,1
        for i in range(length):
            new_sol[i] *= pre
            pre *= nums[i]
            new_sol[length-i-1] *= post
            post *= nums[length-i-1]

        return new_sol
