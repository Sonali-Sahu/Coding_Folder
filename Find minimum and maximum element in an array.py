# link :- https://practice.geeksforgeeks.org/problems/find-minimum-and-maximum-element-in-an-array4428/1
def getMinMax( a, n):
    max = 0
    min = sum(a)
    for i in a:
        if min > i:
            min = i
        if max < i:
            max = i
        
    return [min,max]
    
