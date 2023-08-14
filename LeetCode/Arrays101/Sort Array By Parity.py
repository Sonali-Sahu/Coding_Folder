
Input: nums = [3,1,2,4]
Output: [2,4,3,1]
Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.

# TC = O(n^2)
# SC = O(e+o) = O(n)

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        return [x for x in nums if x%2 == 0 ]+[x for x in nums if x%2 != 0]
