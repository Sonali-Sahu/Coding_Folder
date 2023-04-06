# question link https://practice.geeksforgeeks.org/problems/78a6854c8a2915e05f236aa407dfaa1bbc8ae7d3/1

# only passed 62 test cases
class Solution:
    # Complete this function
    
    #Function to find equilibrium point in the array.
    def equalSum(self,A, N):
        # Your code here
        if len(A) == 1:
            return 1
        else:
            #print("Console till here")
            for i in range(len(A)):
                #print(A[:i],A[i+1:],i-1,i+1,sum(A[:i]),sum(A[i+1:]))
                if sum(A[:i]) == sum(A[i+1:]):
                    return i+1
        return -1
        
# all 1120 test cases passed

class Solution:
    # Complete this function
    
    #Function to find equilibrium point in the array.
    def equalSum(self,A, N):
        if N==1:
            return 1
        a_sum = 0
        for i in range(N):
            a_sum += A[i]
        # doubt on this
        if a_sum ==A[0]:
            return A[0]
        l = 0
        r = 0
        i = 0
        for i in range(N):
            l += A[i]
            if i< N-1:
                r =a_sum-A[i+1]-l
            if l == r:
                return i+2
        return -1
