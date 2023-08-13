https://leetcode.com/explore/learn/card/fun-with-arrays/527/searching-for-items-in-an-array/3250/
# TC = O(n)

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        for i in range(len(arr)):
            if arr[i]/2 in arr[i+1:] or arr[i]*2 in arr[i+1: ]:
                return True
                
        return False
        
