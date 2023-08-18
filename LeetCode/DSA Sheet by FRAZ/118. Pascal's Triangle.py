https://leetcode.com/problems/pascals-triangle/description/

# TC:- O(n*m) - > O(n^2)
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        arr = [[1],[1,1]]
        if numRows == 1:
            return [[1]]
        elif numRows ==2:
            return arr
        else:
            for i in range(3,numRows+1):
                temp_arr = [1]*i
                for j in range(1,i-1):
                    temp_arr[j] = arr[i-2][j-1]+arr[i-2][j]
                arr.append(temp_arr)
            return arr
