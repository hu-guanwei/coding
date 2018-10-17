from copy import deepcopy

class Solution(object):
    def selection_sort(self, array):
        if array is None or len(array) <= 1:
            return array

        arr = deepcopy(array)
        n = len(arr)
        '''
        * * * * * *
        i
         <--j----->
        * * * * * *
          i
           <---j-->
        * * * * * *
            i
             <--j->
        * * * * * *
              i
               <-j>
        * * * * * *
                i
                  j
        '''
        for i in range(0, n - 2 + 1):
            min_index = i
            for j in range(i + 1, n - 1 + 1):
                if arr[j] < arr[min_index]:
                    min_index = j
            if i != min_index:
                arr[i], arr[min_index] = arr[min_index], arr[i]
        return arr

assert(Solution().selection_sort([10,8,9,7,6,4,3,5,1,2]) == [1,2,3,4,5,6,7,8,9,10])
assert(Solution().selection_sort([9,7,5,3,1]) == [1,3,5,7,9])
