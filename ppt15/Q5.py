# You are given a string S, the task is to reverse the string using stack.

# Python3 implementation of
# the above approach

# function to reverse the
# words of the given string
# without using strtok().
def reverse(s):

# create an empty string
# stack
stc = []

# create an empty temporary
# string
temp = ""

# traversing the entire string
for i in range(len(s)):

	if s[i] == ' ':
	
	# push the temporary variable
	# into the stack
	stc.append(temp)
	
	# assigning temporary variable
	# as empty
	temp = ""		

	else:
	temp = temp + s[i]

# for the last word of the string
stc.append(temp)

while len(stc) != 0:

	# Get the words in reverse order
	temp = stc[len(stc) - 1]
	print(temp, end = " ")
	stc.pop()

print()

# Driver code
s = "I Love To Code"
reverse(s)

