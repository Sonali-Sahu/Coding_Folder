# Given an array, for each element find the value of the nearest element 
# to the right which is having a frequency greater than that of the current element.
# If there does not exist an answer for a position, then make the value ‘-1’.


'''NFG function to find the next greater frequency
element for each element in the array'''


def NFG(a, n):

	if (n <= 0):
		print("List empty")
		return []

	# stack data structure to store the position
	# of array element
	stack = [0]*n

	# freq is a dictionary which maintains the
	# frequency of each element
	freq = {}
	for i in a:
		freq[a[i]] = 0
	for i in a:
		freq[a[i]] += 1

	# res to store the value of next greater
	# frequency element for each element
	res = [0]*n

	# initialize top of stack to -1
	top = -1

	# push the first position of array in the stack
	top += 1
	stack[top] = 0

	# now iterate for the rest of elements
	for i in range(1, n):

		''' If the frequency of the element which is
			pointed by the top of stack is greater
			than frequency of the current element
			then push the current position i in stack'''
		if (freq[a[stack[top]]] > freq[a[i]]):
			top += 1
			stack[top] = i

		else:
			''' If the frequency of the element which
			is pointed by the top of stack is less
			than frequency of the current element, then
			pop the stack and continuing popping until
			the above condition is true while the stack
			is not empty'''

			while (top > -1 and freq[a[stack[top]]] < freq[a[i]]):
				res[stack[top]] = a[i]
				top -= 1

			# now push the current element
			top += 1
			stack[top] = i

	'''After iterating over the loop, the remaining
	position of elements in stack do not have the
	next greater element, so print -1 for them'''
	while (top > -1):
		res[stack[top]] = -1
		top -= 1

	# return the res list containing next
	# greater frequency element
	return res


# Driver Code
print(NFG([1, 1, 2, 3, 4, 2, 1], 7))
