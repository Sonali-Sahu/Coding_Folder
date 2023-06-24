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


#Q3 The school cafeteria offers circular and square sandwiches at lunch break, referred to by numbers 0 and 1 respectively.
# All students stand in a queue. Each student either prefers square or circular sandwiches.


class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        while(len(students)!=0):
            if(sandwiches[0] not in students):
                return(len(students))
            if(students[0]==sandwiches[0]):
                students.pop(0)
                sandwiches.pop(0)
            else:
                a=students.pop(0)
                students.append(a)
        return(len(students))

# Q4. 

