from copy import deepcopy

class Solution(object):
    def bubble_sort(self, array):
        '''
        * * * * * *
        <--i--> j
        * * * * *
        <-i-> j
        * * * *
        <i> j
        * * *
        i j
        * *
        j
        i
        '''
        arr = deepcopy(array)
        n = len(arr)
        for j in range(n - 2, 0-1, -1):
            for i in range(0, j + 1):
                if arr[i] > arr[i + 1]:
                    arr[i], arr[i + 1] = arr[i + 1], arr[i]
        return arr
    
assert(Solution().bubble_sort([10,8,9,7,6,4,3,5,1,2]) == [1,2,3,4,5,6,7,8,9,10])
assert(Solution().bubble_sort([9,7,5,3,1]) == [1,3,5,7,9])
