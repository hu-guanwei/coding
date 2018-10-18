from copy import deepcopy

class Solution(object):
    def _merge(self, arr, l, s, r):
        '''
        1 3 5 7 9 2 4 6 8 10
        l         s        r
        i         j
        '''
        aux = []
        i = l
        j = s
        k = 0
        while i <= s - 1 and j <= r:
            if arr[i] < arr[j]:
                aux.append(arr[i])
                i += 1
                k += 1
            else:
                aux.append(arr[j])
                j += 1
                k += 1
        while i <= s - 1:
            aux.append(arr[i])
            i += 1
            k += 1
        while j <= r:
            aux.append(arr[j])
            j += 1
            k += 1
            
        arr[l:r+1] = aux[:]

    def _merge_sort(self, arr, l, r):
        if l >= r:
            return
        m = (l + r) // 2
        self._merge_sort(arr, l, m)
        self._merge_sort(arr, m + 1, r)
        self._merge(arr, l, m + 1, r)

    def merge_sort(self, arr):
        arr2 = deepcopy(arr)
        self._merge_sort(arr2, 0, len(arr2) - 1)
        return arr2
    
arr = [1, 3, 5, 7, 9, 2, 4, 6, 8, 10]
Solution()._merge(arr, 0, 5, len(arr) - 1)
assert(arr == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1]
assert(Solution().merge_sort(arr) == [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
assert(Solution().merge_sort([13, 14, 15, 12, 11, 10, -9, 100]) == [-9, 10, 11, 12, 13, 14, 15, 100])
assert(Solution().merge_sort([5,9,4,0]) == [0, 4, 5, 9])
