# You are given a large integer represented as an integer array digits,
# where each digits[i] is the ith digit of the integer. The digits are ordered from most significant 
# to least significant in left-to-right order. The large integer does not contain any leading 0's
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        str1 = ''.join(str(i) for i in digits)
        str1 = int(str1) + 1
        return map(int,str(str1))
