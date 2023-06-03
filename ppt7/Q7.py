# Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        x=[]
        y=[]
        for i in range(len(s)):
            if x and s[i]=="#":
                x.pop()
            else:
                if s[i]!="#":
                    x.append(s[i])
        for i in range(len(t)):
            if y and t[i]=="#":
                y.pop()
            else:
                if t[i]!="#":
                    y.append(t[i])
        if x==y:
            return True
        return False
