# Given two integer arrays arr1 and arr2, and the integer d, return the distance value between the two arrays.

# The distance value is defined as the number of elements arr1[i] such that there is not any element arr2[j] where |arr1[i]-arr2[j]| <= d.
class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2=sorted(arr2)
        res=0
        for num in arr1:
            idx = bisect.bisect_left(arr2, num)
            lower_within_limits = abs(arr2[min(len(arr2)-1, idx)]-num)>d
            higher_within_limits = abs(arr2[max(0, idx-1)]-num)>d
            if lower_within_limits and higher_within_limits:
                res+=1
        return res
