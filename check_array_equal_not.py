# question link :- https://practice.geeksforgeeks.org/problems/check-if-two-arrays-are-equal-or-not3847/1?page=1&curated[]=1&sortBy=submissions

# time out error 105 testcase passed as remove is called in each loop
class Solution:
    #Function to check if two arrays are equal or not.
    def check(self,A,B,N):
        
        #return: True or False
        #code here
        for i in range(N):
            if A[i] in B:
                B.remove(A[i])
            else:
                return False
        if len(B)==0:
            return True
        else:
            return False
          
# only 2 times sorted is called          
class Solution:
    #Function to check if two arrays are equal or not.
    def check(self,A,B,N):
        
        #return: True or False
        #code here
        A = sorted(A)
        B = sorted(B)
        for i in range(N):
            if A[i] != B[i]:
                return False
      
        return True
