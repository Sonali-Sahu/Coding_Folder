# You are given an inclusive range [lower, upper] and a sorted unique integer array
# nums, where all elements are within the inclusive range.

# A number x is considered missing if x is in the range [lower, upper] and x is not in
# nums.

# Return the shortest sorted list of ranges that exactly covers all the missing
# numbers. That is, no element of nums is included in any of the ranges, and each
# missing number is covered by one of the ranges.

class Solution(object):
  def findMissingRanges(self, nums, lower, upper):
    """
    :type nums: List[int]
    :type lower: int
    :type upper: int
    :rtype: List[str]
    """
    ans = []
    nums = [lower - 1] + nums + [upper + 1]
    for i in range(0, len(nums) - 1):
      if nums[i] + 2 == nums[i + 1]:
        ans.append(str(nums[i] + 1))
      if nums[i + 1] > nums[i] + 2:
        ans.append(str(nums[i] + 1) + "->" + str(nums[i + 1] - 1))
    return ans
