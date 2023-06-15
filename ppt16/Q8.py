# Given an array of integers, the task is to find the maximum absolute difference 
# between the nearest left and the right smaller element of every element in the array.

# **Note:** If there is no smaller element on right side or left side of any element 
#   then we take zero as the smaller element. For example for the leftmost element, 
#   the nearest smaller element on the left side is considered as 0. Similarly,
#   for rightmost elements, the smaller element on the right side is considered as 0.


# Python program to find the difference b/w left and
# right smaller element of every element in the array

# Function to fill left smaller element for every
# element of arr[0..n-1]. These values are filled
# in SE[0..n-1]
def leftsmaller(arr, n, SE):

	# create an empty stack
	sta = []
	# Traverse all array elements
	# compute nearest smaller elements of every element
	for i in range(n):
		
		# Keep removing top element from S while the top
		# element is greater than or equal to arr[i]
		while(sta != [] and sta[len(sta)-1] >= arr[i]):
			sta.pop()

		# Store the smaller element of current element
		if(sta != []):
			SE[i]=sta[len(sta)-1]
		# If all elements in S were greater than arr[i]
		else:
			SE[i]=0

		# push this element
		sta.append(arr[i])

# Function returns maximum difference b/w Left &
# right smaller element
def findMaxDiff(arr, n):
	ls=[0]*n # to store left smaller elements
	rs=[0]*n # to store right smaller elements

	# find left smaller elements of every element
	leftsmaller(arr, n, ls)
	
	# find right smaller element of every element
	# by sending reverse of array
	leftsmaller(arr[::-1], n, rs)

	# find maximum absolute difference b/w LS & RRS
	# In the reversed array right smaller for arr[i] is
	# stored at RRS[n-i-1]
	res = -1
	for i in range(n):
		res = max(res, abs(ls[i] - rs[n-1-i]))
	# return maximum difference b/w LS & RRS
	return res

	
# Driver Program
if __name__=='__main__':
	arr = [2, 4, 8, 7, 7, 9, 3]
	print "Maximum Diff :", findMaxDiff(arr, len(arr))

