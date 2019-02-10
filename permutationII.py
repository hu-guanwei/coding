def dfs(arr, level, res):
    if level == len(arr):
        res.append(arr[:])
        return

    s = set()
    for index in range(level, len(arr)):
        if arr[index] not in s:
            s.add(arr[index])
            arr[level], arr[index] = arr[index], arr[level]
            dfs(arr, level + 1, res)
            arr[level], arr[index] = arr[index], arr[level]
    
res = []
dfs(['a','b','b'], 0, res)
print(res)