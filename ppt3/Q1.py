# Given an integer array nums of length n and an integer target, find three integers
# in nums such that the sum is closest to the target.
# Return the sum of the three integers.

# You may assume that each input would have exactly one solution.


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        closest = nums[0]+nums[1]+nums[2]
        nums.sort()
        for i in range(len(nums)-2):
            l = i+1
            r = len(nums)-1
            while l<r:
                total = nums[i] + nums[l] + nums[r]
                if abs(total-target) < abs(target-closest):
                    closest = total
                if total>target:
                    r-=1
                elif total<target:
                    l+=1
                else:
                    return closest
        return closest
