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

# Q4. You have a RecentCounter class which counts the number of recent requests within a certain time frame.
class RecentCounter:

    def __init__(self):
        self.s = []

    def ping(self, t: int) -> int:
        while self.s and t - self.s[0] > 3000:
            self.s.pop(0)  # remove 1st el if it's 3000+ away from t
        self.s.append(t)
        return len(self.s) 
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)



# Q5. There are n friends that are playing a game. The friends are sitting in a circle and are numbered 
# from 1 to n in clockwise order. More formally, moving clockwise from the ith friend brings you 
# to the (i+1)th friend for 1 <= i < n, and moving clockwise from the nth friend brings you to the 1st friend


class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        q = collections.deque([i for i in range(1, n + 1)])
        
        while len(q) > 1:
            for i in range(k - 1):
                val = q.popleft()
                q.append(val)
            
            q.popleft()
        
        return q.popleft()

#Q6. You are given an integer array deck. There is a deck of cards where every card has a 
# unique integer. The integer on the ith card is deck[i].
















