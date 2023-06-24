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















