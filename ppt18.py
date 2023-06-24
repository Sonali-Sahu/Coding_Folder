#Q1. Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals,
# and return an array of the non-overlapping intervals that cover all the intervals in the input.

from heapq import *

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = self.sortByStartTime(intervals)
        result = [intervals.pop(0)]
        
        while len(intervals) != 0:
            topStack = result.pop()
            firstInQueue = intervals.pop(0)
            
            # the two dont merge
            if topStack[1] < firstInQueue[0]:
                result.append(topStack)
                result.append(firstInQueue)
            
            # the two merge
            else:
                startTime = topStack[0]
                endTime = max(topStack[1], firstInQueue[1])
                result.append([startTime, endTime])
        
        return result
    
    # sort the intervals by start times
    def sortByStartTime(self, intervals):
        h = []
        result = []
        
        for item in intervals:
            heappush(h, (item[0], item[1]))
                    
        while len(h) != 0:
            item = heappop(h)
            result.append([item[0], item[1]])
            
        return result



#Q2 Given an array nums with n objects colored red, white, or blue, sort them in-place so
# that objects of the same color are adjacent, with the colors in the order red, white, and blue.
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        low = 0
        high = n - 1
        i = 0

        while i <= high:
            
            if nums[i] == 0:
                nums[i], nums[low] = nums[low], nums[i]
                low += 1
            
            elif nums[i] == 2:
                nums[i], nums[high] = nums[high], nums[i]
                high -= 1
                i -= 1
            i += 1


#Q3. You are a product manager and currently leading a team to develop a new product.
# Unfortunately, the latest version of your product fails the quality check.
# Since each version is developed based on the previous version, all the versions after a bad version are also bad.
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        # binary search / 2 pointers
        left = 1
        right = n
        result = 1
        
        while left<=right:
            mid = (left+right)//2
            if isBadVersion(mid) == False:
                left = mid+1
            else:
                right = mid-1
                result = mid
                
        return result


#Q4. Given an integer array nums, return the maximum difference between two successive
# elements in its sorted form. If the array contains less than two elements, return 0.

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums.sort()
        n=len(nums)
        m=0
        for i in range(n-1):
            m=max(m,abs(nums[i]-nums[i+1]))
        return m

#Q5. Given an integer array nums, return true if any value appears 
# at least twice in the array, and return false if every element is distinct.

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        new_list = set(nums)
        if len(new_list)<len(nums):
            return True
        else:
            return False


#Q6. There are some spherical balloons taped onto a flat wall that represents the XY-plane. 
# The balloons are represented as a 2D integer array points where points[i] = [xstart, xend]
# denotes a balloon whose horizontal diameter stretches between xstart and xend. You do not know the exact y-coordinates of the balloons.

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        # sort by end point   
        points.sort(key = lambda x: x[1])
        end = points[0][1]
        count = 1
        # iterate and count arrows
        for s,e in points[1:]:
            if s > end:
                count += 1
                end = e
        
        return count
#Q7.Given an integer array nums, return the length of the longest strictly increasing
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        arr = [nums.pop(0)]                  
        for n in nums:                    
            
            if n > arr[-1]:             
                arr.append(n)

            else:                            
                arr[bisect_left(arr, n)] = n 

        return len(arr) 


#Q8. Given an array of n integers nums, a 132 pattern is a subsequence of three
# integers nums[i], nums[j] and nums[k] such that i < j < k and nums[i] < nums[k] < nums[j].

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        s2 = float('-inf')
        for i in nums[::-1]:
            if i<s2: return True
            while stack and i>stack[-1]: 
                s2 = stack.pop()
            stack.append(i)
        return False
