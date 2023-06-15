# Given a sequence of n strings, the task is to check if any two similar words come together 
# and then destroy each other then print the number of words left in the sequence after this pairwise destruction.

# Python3 program to remove consecutive
# same words

# Function to find the size of
# manipulated sequence
def removeConsecutiveSame(v):

	n = len(v)

	# Start traversing the sequence
	i = 0
	while(i < n - 1):
		
		# Compare the current string with
		# next one Erase both if equal
		if ((i + 1) < len(v)) and (v[i] == v[i + 1]):
		
			# Erase function delete the element and
			# also shifts other element that's why
			# i is not updated
			v = v[:i]
			v = v[:i]

			# Update i, as to check from previous
			# element again
			if (i > 0):
				i -= 1

			# Reduce sequence size
			n = n - 2
		
		# Increment i, if not equal
		else:
			i += 1
	
	# Return modified size
	return len(v[:i - 1])
	
# Driver Code
if __name__ == '__main__':
	v = ["tom", "jerry", "jerry", "tom"]
	print(removeConsecutiveSame(v))
