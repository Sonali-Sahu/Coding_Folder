# A permutation perm of n + 1 integers of all the integers in the range [0, n]
# can be represented as a string s of length n where:

# - s[i] == 'I' if perm[i] < perm[i + 1], and
# - s[i] == 'D' if perm[i] > perm[i + 1].



class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        L,ic,dc=[],0,len(s)
        for i in s:
            if i=='I':
                L.append(ic)
                ic+=1
            else:
                L.append(dc)
                dc-=1
        if s[-1]=='I':L.append(ic)
        else:L.append(dc)
        return L
