# Given a set represented as a string, write a recursive code to print all subsets of it. The subsets can be printed in any order.

# **Example 1:**

# Input :  set = “abc”

# Output : { “”, “a”, “b”, “c”, “ab”, “ac”, “bc”, “abc”}

# **Example 2:**

# Input : set = “abcd”

# Output : { “”, “a” ,”ab” ,”abc” ,”abcd”, “abd” ,”ac” ,”acd”, “ad” ,”b”, “bc” ,”bcd” ,”bd” ,”c” ,”cd” ,”d” }



def printSubsequence(input, output):
	if len(input) == 0:
		print(output, end=' ')
		return

	printSubsequence(input[1:], output+input[0])
	printSubsequence(input[1:], output)

output = ""
input = "abc"

printSubsequence(input, output)
