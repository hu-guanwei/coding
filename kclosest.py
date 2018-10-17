class Solution(object):
    def kclosest(self, arr, target, k):
        if arr is None or len(arr) == 0:
            return []
        if k == 0:
            return []

        l = 0
        r = len(arr) - 1
        # stop when l is next to r
        while l < r - 1:
            m = (l + r) // 2
            if target < arr[m]:
                r = m
            else:
                l = m

        cnt = 0
        res = []
        # stop when cnt == k and reach edge
        while l >= 0 and r <= len(arr) - 1 and cnt < k:
            if abs(arr[l] - target) < abs(arr[r] - target):
                res.append(arr[l])
                l -= 1
            else:
                res.append(arr[r])
                r += 1
            cnt += 1
            
        while l >= 0 and cnt < k:
            res.append(arr[l])
            l -= 1
            cnt += 1
        while r <= len(arr) - 1 and cnt < k:
            res.append(arr[r])
            r += 1
            cnt += 1
        return res

print(Solution().kclosest([1,2,3,4,5,6,7,8,9,10], 5, 4))
print(Solution().kclosest([1,2,3,4,5,6,7,8,9,10], 1, 4))        
