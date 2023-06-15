# Given a stack with push(), pop(), and empty() operations, 
# The task is to delete the middle element of it without using any additional data structure.

import math

st = []
st.append('1')
st.append('2')
st.append('3')
st.append('4')
st.append('5')
st.append('6')
st.append('7')

v = []

while(len(st) > 0):
	v.append(st[0])
	del st[0]
	
n = len(v)

if n%2==0:
	target = math.floor(n/2)
	for i in range(0, n):
		if i==target:
			continue
		st.append(v[i])
else:
	target = math.floor(n/2)
	for i in range(0, n):
		if i==target:
			continue
		st.append(v[i])

print("Printing stack after deletion of middle:", end = " ")

while (len(st) > 0):
	p = st[0]
	del st[0]
	print(p, end = " ")

