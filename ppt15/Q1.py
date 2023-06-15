# Given an array arr[ ] of size N having elements, the task is to find the next greater element
# for each element of the array in order of their appearance in the array.Next greater element of
# an element in the array is the nearest element on the right which is greater than 
# the current element.If there does not exist next greater of current element, then next greater
# element for current element is -1. For example, next greater of the last element is always -1.

# Python program to print next greater element using stack

# Stack Functions to be used by printNGE()


def createStack():
	stack = []
	return stack


def isEmpty(stack):
	return len(stack) == 0


def push(stack, x):
	stack.append(x)


def pop(stack):
	if isEmpty(stack):
		print("Error : stack underflow")
	else:
		return stack.pop()



def printNGE(arr):
	s = createStack()
	element = 0
	next = 0

	push(s, arr[0])

	for i in range(1, len(arr), 1):
		next = arr[i]

		if isEmpty(s) == False:
			element = pop(s)

			while element < next:
				print(str(element) + " -- " + str(next))
				if isEmpty(s) == True:
					break
				element = pop(s)

			if element > next:
				push(s, element)

		push(s, next)

	while isEmpty(s) == False:
		element = pop(s)
		next = -1
		print(str(element) + " -- " + str(next))


# Driver code
arr = [1, 3, 2, 4]
printNGE(arr)
