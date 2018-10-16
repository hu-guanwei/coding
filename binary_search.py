class Solution(object):
    def binary_search(self, arr, target):
        if arr is None or len(arr) == 0:
            return -1
        l = 0
        r = len(arr) - 1
        while l <= r:
            m = (l + r) // 2
            if target == arr[m]:
                return m
            elif target < arr[m]:
                r = m - 1
            else:
                l = m + 1
        return -1

assert(Solution().binary_search([1,2,3,4,5,6,7,8,9], 9) == 8)
assert(Solution().binary_search([1,3,4,5,6,7,8,9,100,200,1000], 100) == 8)

