# Given an array of integers arr, return *true if and only if it is a valid mountain array*.

# Recall that arr is a mountain array if and only if:

# - arr.length >= 3
# - There exists some i with 0 < i < arr.length - 1 such that:


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr)<3:return False
        l=len(arr)
        i,j=0,l-1
        while i<j and arr[i]<arr[i+1]:
            i+=1
        while j>0 and arr[j]<arr[j-1]:
            j-=1
        if i==j and j!=l-1 and i!=0:return True
        return False
