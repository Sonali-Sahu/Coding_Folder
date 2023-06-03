# An integer array original is transformed into a **doubled** array changed by appending
# **twice the value** of every element in original, and then randomly **shuffling** the resulting array.

# Given an array changed, return original *if* changed *is a **doubled** array. If* changed *is not a
# **doubled** array, return an empty array. The elements in* original *may be returned in **any** order*.

class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed)%2!=0:return []
        changed.sort()
        c=Counter(changed)
        ans=[]
        if c[0]%2==0:
            ans+=[0]*(c[0]//2)
            
        for i in c:
            if i==0 or c[i]==0:
                continue
            elif (i*2 not in c) or c[i]>c[i*2]:
                return []
            c[i*2]-=c[i]
            ans+=[i]*c[i]
                
        return ans
