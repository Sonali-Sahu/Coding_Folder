# The product sum of two equal-length arrays a and b is equal to the sum
# of a[i] * b[i] for all 0 <= i < a.length (0-indexed).

# The **product sum** of two equal-length arrays a and b is equal to the sum of a[i] * b[i] for all 0 <= i < a.length (**0-indexed**).

# - For example, if a = [1,2,3,4] and b = [5,2,3,1], the **product sum** would be 1*5 + 2*2 + 3*3 + 4*1 = 22.

class Solution:
    def minProductSum(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort(reverse=True)

        res = 0
        for a, b in zip(nums1, nums2):
            res += a * b
        return res
