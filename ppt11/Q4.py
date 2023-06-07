# Given an array of integers `nums` containing `n + 1` integers where each integer is in the range `[1, n]` inclusive.

# There is only **one repeated number** in `nums`, return *this repeated number*.

# You must solve the problem **without** modifying the array `nums` and uses only constant extra space.




class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        jk = nums[0]
        jh = nums[0]

        while True:
            jk = nums[jk]
            jh = nums[nums[jh]]
            if jk == jh:
                break

        jk = nums[0]
        while jk != jh:
            jk = nums[jk]
            jh = nums[jh]

        return jk
