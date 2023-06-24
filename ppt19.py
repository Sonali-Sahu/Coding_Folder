#Q1. You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        new=[]
        for i in lists:
            while(i):
                new.append(i.val)
                i = i.next

        # Sort the list and reverse it
        a=sorted(new,reverse=True)
    
        # Create a ListNode from list
        final=None
        for i in a:
            final=ListNode(i,final)
        return final

#Q2. Given an integer array nums, return an integer array counts where counts[i] is the number of smaller elements to the right of nums[i].

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        arr, ans = sorted(nums), []    
        
        for num in nums:
            i = bisect_left(arr,num)  
            ans.append(i)         
            del arr[i]
            
        return ans       



#Q3. Given an array of integers `nums`, sort the array in ascending order and return it.

# You must solve the problem **without using any built-in** functions in `O(nlog(n))` time complexity and with the smallest space complexity possible.

# check it again

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.mergeSort(nums)


    def mergeSort(self, nums):
        def recur(left, right):
            nonlocal tmp
            if left>=right: return ## base case
            
            mid = (left+right)//2
            recur(left, mid); recur(mid+1, right) ## recursive calls
            
            pl, pr, pt = left, mid+1, left ## left, right, tmp pointer
            while pl<=mid and pr<=right: ## merge
                if nums[pl]<=nums[pr]:
                    tmp[pt]=nums[pl]; pl+=1
                else:
                    tmp[pt]=nums[pr]; pr+=1
                pt += 1
            if pl<mid+1: ## merge rest
                tmp[pt:right+1] = nums[pl:mid+1] 
            elif pr<right+1:
                tmp[pt:right+1] = nums[pr:right+1]
            nums[left:right+1] = tmp[left:right+1] ## copy back
            
        l=len(nums); tmp=[None]*l
        recur(0, l-1)
        return nums



#Q4. Given an array of random numbers, Push all the zero’s of a given array to the end of the array.
      # For example, if the given arrays is {1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0}

A = [5, 6, 0, 4, 6, 0, 9, 0, 8]
n = len(A)
B = [0] * n
j = 0
count = 0
 
for i in range(n):
    if A[i] != 0:
        B[j] = A[i]
        j += 1
    else:
        count += 1
 
while count > 0:
    B[j] = 0
    count -= 1
    j += 1
 
for i in range(n):
    A[i] = B[i]
 
for i in range(n):
    print(A[i], end=' ')


#Q5. 


# Python3 program to rearrange
# positive and negative integers
# in alternate fashion and
# maintaining the order of positive
# and negative numbers
# rotates the array to right by once
# from index 'outOfPlace to cur'


def rightRotate(arr, n, outOfPlace, cur):
	temp = arr[cur]
	for i in range(cur, outOfPlace, -1):
		arr[i] = arr[i - 1]
	arr[outOfPlace] = temp
	return arr


def rearrange(arr, n):
	outOfPlace = -1
	for index in range(n):
		if(outOfPlace >= 0):
			if((arr[index] >= 0 and arr[outOfPlace] < 0) or
			(arr[index] < 0 and arr[outOfPlace] >= 0)):
				arr = rightRotate(arr, n, outOfPlace, index)
				if(index-outOfPlace > 2):
					outOfPlace += 2
				else:
					outOfPlace = - 1

		if(outOfPlace == -1):
			if((arr[index] >= 0 and index % 2 == 0) or
			(arr[index] < 0 and index % 2 == 1)):
				outOfPlace = index
	return arr


# Driver Code
arr = [-5, -2, 5, 2, 4,
	7, 1, 8, 0, -8]

print("Given Array is:")
print(arr)

print("\nRearranged array is:")
print(rearrange(arr, len(arr)))


#Q6.  Given two sorted arrays, the task is to merge them in a sorted manner.

def mergeArrays(arr1, arr2, n1, n2, arr3):
    i = 0
    j = 0
    k = 0
    while(i < n1):
        arr3[k] = arr1[i]
        k += 1
        i += 1
 
    while(j < n2):
        arr3[k] = arr2[j]
        k += 1
        j += 1
 

    return arr3.sort()

#Q7. Given two integer arrays nums1 and nums2, return an array of their intersection.
# Each element in the result must be unique and you may return the result in any order.


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) < len (nums2):
            nums1,nums2 = nums2,nums1

        res = []
        nums1.sort()
        nums2 = set(nums2)
        for i in nums2:
            l,r = 0, len(nums1)-1
            while l<= r:
                m = (l+r)>>1
                if nums1[m] == i:
                    res.append(i)
                    break
                else:
                    if nums1[m] < i:
                        l = m + 1
                    else: 
                        r = m -1
        return res


#Q8. Given two integer arrays nums1 and nums2, return an array of their intersection.
# Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()

        n1 = len(nums1)
        n2 = len(nums2)

        nums1.append(inf)
        nums2.append(inf)

        i = j = 0
        ans = []
        while i != n1 and j != n2:
            if nums1[i] == nums2[j]:
                ans.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j+=1
        return ans




