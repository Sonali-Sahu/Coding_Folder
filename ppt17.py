# Q1.Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.


class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = {}
        for c in s:
            freq[c] = freq.get(c, 0) + 1
        for i in range(len(s)):
            if freq[s[i]] == 1:
                return i
        return -1



#Q2.Given a circular integer array nums of length n, return the maximum possible sum of a non-empty subarray of nums.

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        maxSum,minSum,curMin,curMax,sum=(nums[0],nums[0],0,0,0)
        for val in nums:
            curMax=curMax+val if curMax+val>=val else val
            maxSum=max(curMax,maxSum)
            curMin=curMin+val if curMin+val<=val else val
            minSum=min(minSum,curMin)
            sum+=val
        return maxSum if sum==minSum else max(maxSum,sum-minSum)


#Q3






