# Given a string S, the task is to write a program to print 
# all permutations of a given string.

# **Example 1:**

# ***Input:***

# *S = “ABC”*

# ***Output:***

# *“ABC”, “ACB”, “BAC”, “BCA”, “CBA”, “CAB”*

# **Example 2:**

# ***Input:***

# *S = “XY”*

# ***Output:***

# *“XY”, “YX”*

def permute(s, answer):
	if (len(s) == 0):
		print(answer, end=" ")
		return

	for i in range(len(s)):
		ch = s[i]
		left_substr = s[0:i]
		right_substr = s[i + 1:]
		rest = left_substr + right_substr
		permute(rest, answer + ch)


# Driver Code
answer = ""

s = "ABC"

permute(s, answer)
