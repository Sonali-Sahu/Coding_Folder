# You are given an m x n matrix M initialized with all 0's and an array of operations ops, where ops[i] = [ai, bi] means M[x][y] should be
# incremented by one for all 0 <= x < ai and 0 <= y < bi.

class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        return min([x for x,y in ops])*min([y for x,y in ops]) if ops else m*n
