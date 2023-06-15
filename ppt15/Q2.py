# Given an array a of integers of length n, find the nearest smaller number for every element 
# such that the smaller element is on left side.If no small element present on the left print -1.


class Solution:
    def leftSmaller(self, n, a):
        stack=[]
        ans=[]
        for i in range(n):
            while len(stack)!=0 and stack[-1]>=a[i]:
                stack.pop()
            if len(stack)==0:
                ans.append(-1)
            else:
                ans.append(stack[-1])
            stack.append(a[i])
        return ans
