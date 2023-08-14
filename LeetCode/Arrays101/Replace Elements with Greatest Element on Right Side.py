https://leetcode.com/explore/learn/card/fun-with-arrays/511/in-place-operations/3259/

Input: arr = [17,18,5,4,6,1]
Output: [18,6,6,6,1,-1]
Explanation: 
- index 0 --> the greatest element to the right of index 0 is index 1 (18).
- index 1 --> the greatest element to the right of index 1 is index 4 (6).
- index 2 --> the greatest element to the right of index 2 is index 4 (6).
- index 3 --> the greatest element to the right of index 3 is index 4 (6).
- index 4 --> the greatest element to the right of index 4 is index 5 (1).
- index 5 --> there are no elements to the right of index 5, so we put -1.

# TC = O(n)
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # length of array
        n = len(arr) - 1
        arr[n],max_ele = -1,arr[n]
        
        for i in reversed(range(n)):
            if arr[i] > max_ele:
                arr[i],max_ele = max_ele,arr[i]
            else:
                arr[i] = max_ele
                
        return arr
