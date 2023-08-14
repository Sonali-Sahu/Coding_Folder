https://leetcode.com/explore/learn/card/fun-with-arrays/523/conclusion/3270/

# TC = O(n)
# but time limit exceeded

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        new_list  = []
        for i in range(1,len(nums)+1):
            if i not in nums:
                new_list.append(i)
                
        return new_list
