https://leetcode.com/problems/3sum/description/

# TC = O(n^2)
# Brute  Force
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = set()

        # making p,n,z list to segregate all the values
        p,n,z = [],[],[]
        for i in nums:
            if i > 0:
                p.append(i)
            elif i < 0:
                n.append(i)
            else:
                z.append(i)

        if len(z) >=3:
            res.add((0,0,0))

        P,N = set(p),set(n)

        if z:
            for ele in P:
                if -1*ele in N:
                    res.add((-1*ele,0,ele))

        # for 2 numbers from P and 1 num from N
        for i in range(len(p)):
            for j in range(i+1,len(p)):
                target = -1 * (p[i]+p[j])
                if target in N:
                    res.add(tuple(sorted([p[i],p[j],target])))

        # for 2 N and 1 P
        for i in range(len(n)):
            for j in range(i+1,len(n)):
                target = -1 * (n[i]+n[j])
                if target in P:
                    res.add(tuple(sorted([n[i],n[j],target])))
        return list(res)


