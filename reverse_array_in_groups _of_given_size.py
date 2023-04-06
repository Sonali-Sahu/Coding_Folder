# question :- https://practice.geeksforgeeks.org/problems/reverse-array-in-groups0255/1?page=1&curated[]=1&sortBy=submissions
def reverseInGroups(self, arr, n, k):
		# code here
		i = 0
     
        while(i<n):
         
            left = i
     
            # To handle case when k is not
            # multiple of n
            right = min(i + k - 1, n - 1)
     
            # Reverse the sub-array [left, right]
            while (left < right):
                 
                arr[left], arr[right] = arr[right], arr[left]
                left+= 1;
                right-=1
            i+= k
