# Given a string str, the task is to print all the permutations of str.
# A permutation is an arrangement of all or part of a set of objects, with regard to the order of the arrangement. 
# For instance, the words ‘bat’ and ‘tab’ represents two distinct permutation (or arrangements) of a similar three letter word.


def permute(s, answer):
    if (len(s) == 0):
        print(answer, end="  ")
        return
 
    for i in range(len(s)):
        ch = s[i]
        left_substr = s[0:i]
        right_substr = s[i + 1:]
        rest = left_substr + right_substr
        permute(rest, answer + ch)
 
answer = ""
 
s = "ABC"
permute(s, answer)
