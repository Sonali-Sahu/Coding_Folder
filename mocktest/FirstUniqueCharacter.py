def firstuniquecharacter(s:str) -> int:
    def count(word,key):
        c = 0
        for i in word:
            if i == key:
                c+=1
        return c

    for i in range(len(s)):
        if count(s, s[i])==1:
            return i
        
    return -1


print(firstuniquecharacter("loveleetcode"))

# but time limit exceeded

class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i,key in enumerate(s):
            if s.count(key) == 1:
                return i

        return -1
        
        
        
# SO used built-in functions 
