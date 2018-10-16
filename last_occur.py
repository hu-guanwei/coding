class Solution(object):
    def last_occur(self, arr, target):
        if arr is None or len(arr) == 0:
            return -1
        l = 0
        r = len(arr) - 1
        # stop when l == r - 1
        while l < r -1:
            m = (l + r) // 2
            if target == arr[m]:
                # then elements in arr[0, m-1] (closed interval)
                # cannot be the last occurance of our target
                l = m
                # so, continue searching in arr[m, end]
            elif target < arr[m]:
                r = m - 1
            else:
                l = m + 1
                
        if target == arr[r]:
            return r
        elif target == arr[l]:
            return l
        return -1
            
assert(Solution().last_occur([1,2,3,3,4,5,6,7], 10) == -1)
assert(Solution().last_occur([1,1,2,2,3,3], 1) == 1)
assert(Solution().last_occur([1,1,2,2,3,3], 2) == 3)
assert(Solution().last_occur([1,1,2,2,3,3], 3) == 5)

