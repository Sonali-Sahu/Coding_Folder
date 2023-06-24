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

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        L, Q, _ = len(deck)-1, collections.deque(), deck.sort()
        for _ in range(L): 
            Q.appendleft(deck.pop()), Q.appendleft(Q.pop())
        return deck + list(Q)

#Q7. Design a queue that supports `push` and `pop` operations in the front, middle, and back.

# Implement the `FrontMiddleBack` class:


class FrontMiddleBackQueue:

    def __init__(self):
        self.q1 = deque([])
        self.q2 = deque([])

    def pushFront(self, val: int) -> None:
        self.q1.appendleft(val)
        if len(self.q1) - len(self.q2) == 2:
            self.q2.appendleft(self.q1.pop())

    def pushMiddle(self, val: int) -> None:
        if len(self.q1) - len(self.q2) == 1:
            self.q2.appendleft(self.q1.pop())
        self.q1.append(val)

    def pushBack(self, val: int) -> None:
        # append first so that if q1, q2 are empty q2 can have something to popleft 
        self.q2.append(val)
        if len(self.q1) == len(self.q2) - 1:
            self.q1.append(self.q2.popleft())

    def popFront(self) -> int:
        if len(self.q1) == 0:
            return -1
        if len(self.q1) == len(self.q2):
            self.q1.append(self.q2.popleft())
        return self.q1.popleft()

    def popMiddle(self) -> int:
        if len(self.q1) == 0:
            return -1
        val = self.q1.pop()
        if len(self.q1) + 1 == len(self.q2):
            self.q1.append(self.q2.popleft())
        return val   

    def popBack(self) -> int:
        if len(self.q2) == 0:
            if len(self.q1) == 1:
                return self.q1.pop()
            return -1
        val = self.q2.pop()
        if len(self.q2) + 2 == len(self.q1):
            self.q2.appendleft(self.q1.pop())
        return val
        


# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()


# Q8. For a stream of integers, implement a data structure that checks if the last k integers parsed in the stream are equal to value.


from collections import deque
class DataStream:

    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.deque = deque()
        self.count = 0
        

    def consec(self, num: int) -> bool:
        if len(self.deque) == self.k:
            if self.deque[0] == self.value:
                self.count -= 1
            self.deque.popleft()
        self.deque.append(num)
        if num == self.value:
            self.count += 1
        return self.count == self.k
        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)














