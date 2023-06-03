# Given an array of characters chars, compress it using the following algorithm:

# Begin with an empty string s. For each group of **consecutive repeating characters** in chars:

# - If the group's length is 1, append the character to s.
# - Otherwise, append the character followed by the group's length.

class Solution:
    def compress(self, chars: List[str]) -> int:
        d=[]
        c=1
        for i in range(1,len(chars)):
            if chars[i]==chars[i-1]:
                c+=1
            else:
                d.append([chars[i-1],c])
                c=1
        d.append([chars[-1],c]) 
        i=0
        for k,v in d:
            chars[i]=k
            i+=1
            if v>1:
                for item in str(v):
                    chars[i]=str(item)
                    i+=1
        return i
