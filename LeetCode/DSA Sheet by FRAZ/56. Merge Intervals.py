https://leetcode.com/problems/merge-intervals/description/

TC = O(n)
SC = O(n)
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # first step sort
        intervals.sort(key= lambda x:x[0])
        new_array = []
        for i in intervals:
            if not new_array or new_array[-1][-1] < i[0]:
                new_array.append(i)
            else:
                new_array[-1][-1] = max(new_array[-1][-1],i[-1])
        return new_array
