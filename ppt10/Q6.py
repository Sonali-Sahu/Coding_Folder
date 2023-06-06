# The tower of Hanoi is a famous puzzle where we have three rods and N disks. The objective of the puzzle is to move the entire stack to another rod. 
# You are given the number of discs N. Initially, these discs are in the rod 1. 
# You need to print all the steps of discs movement so that all the discs reach the 3rd rod.
# Also, you need to find the total moves.
# Note: The discs are arranged such that the top disc is numbered 1 and the bottom-most disc is numbered N.
# Also, all the discs have different sizes and a bigger disc cannot be put on the top of a smaller disc.
# Refer the provided link to get a better clarity about the puzzle.


class Solution:
    def toh(self, N, fromm, to, aux):
        # Your code here
        if N==1:
            print('move disk',N,'from rod',fromm,'to rod',to)
            return 1
            
        count=self.toh(N-1,fromm,aux,to)
        print('move disk',N,'from rod',fromm,'to rod',to)
        count+=self.toh(N-1,aux,to,fromm)
        return count+1 
