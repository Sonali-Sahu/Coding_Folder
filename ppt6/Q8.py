# Given two [sparse matrices](https://en.wikipedia.org/wiki/Sparse_matrix) mat1 of size m x k and mat2 of size k x n,
# return the result of mat1 x mat2. You may assume that multiplication is always possible.


class Solution(object):
  def multiply(self, A, B):
    """
    :type A: List[List[int]]
    :type B: List[List[int]]
    :rtype: List[List[int]]
    """
    ret = [[0 for j in range(len(B[0]))] for i in range(len(A))]

    for i, row in enumerate(A):
      for k, a in enumerate(row):
        if a:
          for j, b in enumerate(B[k]):
            if b:
              ret[i][j] += a * b
    return ret
