class Solution(object):
    def first_occur(self, arr, target):
        if arr is None or len(arr) == 0:
            return -1

        l = 0
        r = len(arr) - 1
        while l < r - 1:
            m = (l + r) // 2
            if target == arr[m]:
                # then arr[m+1, :] cannot be the 1st occurance of target
                r = m
            elif target < arr[m]:
                # then arr[m, :] cannot ...
                r = m - 1
            else:
                l = m + 1

        # post processing
        if target == arr[l]:
            return l
        elif target == arr[r]:
            return r
        return -1
            

            
assert(Solution().first_occur([1,2,3,3,4,5,6,7], 3) == 2)
assert(Solution().first_occur([1,2,3,3,4,4,6,7], 4) == 4)

