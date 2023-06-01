#  A permutation of an array of integers is an arrangement of its members into a
# sequence or linear order.

# For example, for arr = [1,2,3], the following are all the permutations of arr:
# [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].

# The next permutation of an array of integers is the next lexicographically greater
# permutation of its integer. More formally, if all the permutations of the array are
# sorted in one container according to their lexicographical order, then the next
# permutation of that array is the permutation that follows it in the sorted container.

# If such an arrangement is not possible, the array must be rearranged as the
# lowest possible order (i.e., sorted in ascending order).



class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if nums==[] or nums == None or len(nums)==1:
            return
        
        l = len(nums)-1
        i = l
        while (nums[i-1]>=nums[i] and i>0):
            i-=1
        
        if i==0:
            nums.sort()
            return 
        
        start = i-1
        last = l
        p = i-1
        next_to_start = i
     
        while p+1<=last:
            p+=1
            if nums[p] > nums[start] and nums[p] <= nums[next_to_start]:
                next_to_start = p
        nums[start],nums[next_to_start] = nums[next_to_start],nums[start]
        f = i
        b = l
        while f<=b:
            nums[f],nums[b] = nums[b],nums[f]
            f+=1
            b-=1
            
        return 
