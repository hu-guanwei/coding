from copy import deepcopy

class Solution(object):
    def _partition(self, arr, l, r):
        pivot = arr[l]
        '''
        * * * * * *
        l         r
        i k         j

        closed interval
        arr[l+1, i] < pivot
        arr[k, j-1] to be determined
        arr[j, r] >= pivot
        '''

        i = l
        k = i + 1
        j = r + 1

        # stop when k = j
        while k < j:
            if arr[k] < pivot:
                i += 1
                k += 1
            else:
                arr[k], arr[j - 1] = arr[j - 1], arr[k]
                j -= 1
        arr[l], arr[i] = arr[i], arr[l]
        return i
    
    def _quick_sort(self, arr, l, r):
        if l >= r:
            return
        p = self._partition(arr, l, r)
        self._quick_sort(arr, l, p - 1)
        self._quick_sort(arr, p + 1, r)

    def quick_sort(self, arr):
        arr2 = deepcopy(arr)
        self._quick_sort(arr2, 0, len(arr)- 1)
        return arr2
    
arr = [5, 6, 8, 9, 7, 10, 1, 2, 4, 3,]
Solution()._partition(arr, 0, len(arr) - 1)
print(arr)
assert(Solution().quick_sort(arr) == [1,2,3,4,5,6,7,8,9,10])
assert(Solution().quick_sort([38, 76, 99, -1, 100]) == [-1, 38, 76, 99,  100])
assert(Solution().quick_sort([98, 97, 96, 95, 99, 94, 100]) == [94, 95, 96, 97, 98, 99, 100])
