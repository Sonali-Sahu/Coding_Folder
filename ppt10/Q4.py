# Given a string calculate length of the string using recursion.

def lenRecur(s):
    if s =='':
        return 0
    else:
        print(lenRecur(s[1:]))
        return 1 + lenRecur(s[1:])

print(lenRecur("abcd"))
