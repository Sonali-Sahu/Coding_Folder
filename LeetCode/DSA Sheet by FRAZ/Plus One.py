https://leetcode.com/problems/plus-one/description/

# took hint 

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        for i in reversed(range(len(digits))):
            if digits[i] < 9 :
                digits[i] +=1
                # increase the number by 1 and return it
                return digits
            else:
                digits[i]=0
        return [1]+digits
