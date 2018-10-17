from copy import deepcopy

class Solution(object):
    def insertion_sort(self, array):
        if array is None or len(array) <= 1:
            return array
        '''
        * * * * * *
          i
          j
        * * * * * *
            i
          <j>
        * * * * * *
              i
          <-j->
        * * * * * *
                i
          <--j-->
        * * * * * *
                  i
          <---j--->
        '''
        arr = deepcopy(array)
        n = len(arr)
        for i in range(1, n - 1 + 1):
            j = i
            while j >= 1:
                if arr[j] < arr[j - 1]:
                    arr[j], arr[j - 1] = arr[j - 1], arr[j]
                    j -= 1
                else:
                    break
        return arr

assert(Solution().insertion_sort([10,8,9,7,6,4,3,5,1,2]) == [1,2,3,4,5,6,7,8,9,10])
assert(Solution().insertion_sort([9,7,5,3,1]) == [1,3,5,7,9])
