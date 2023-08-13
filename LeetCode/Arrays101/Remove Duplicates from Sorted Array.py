https://leetcode.com/explore/learn/card/fun-with-arrays/526/deleting-items-from-an-array/3248/

# TC = O(n)
# SC = O(n)
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        c = 1
        ele = nums [0]
        new_list = [ele]
        for i in nums:
            if ele != i:
                c +=1
                ele = i
                new_list.append(i)
                
        nums[:] = new_list
        
        return c

# TC = O(n)
# no extra space consumed
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        c = 1
        ele = nums [0]
        for i in nums:
            if ele != i:
                c +=1
                ele = i
                nums[c-1] = i         
        return c
