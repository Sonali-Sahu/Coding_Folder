https://leetcode.com/explore/learn/card/fun-with-arrays/527/searching-for-items-in-an-array/3251/

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
