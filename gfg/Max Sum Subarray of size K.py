https://practice.geeksforgeeks.org/problems/max-sum-subarray-of-size-k5313/1

# TC :- O(n)

class Solution:
    def maximumSumSubarray (self,K,Arr,N):
        # code here 
        max_sum = 0
        i = 0
        j = 0
        sum_l = 0
        while(j<N):
            # print('i,j',i,j)
            if (j-i) != K:
                sum_l += Arr[j]
                j += 1
                # print('intermediate sum',sum_l)
            else:                
                sum_l = sum_l - Arr[i]
                i += 1
            if max_sum < sum_l:
                max_sum = sum_l
                # print('max_sum',max_sum)
        return max_sum
