def dfs(arr, level, res):
    if level == len(arr):
        res.append(arr[:])
        return

    for index in range(level, len(arr)):
        # swap - swap
        arr[index], arr[level] = arr[level], arr[index]
        dfs(arr, level + 1, res)
        arr[index], arr[level] = arr[level], arr[index]

res = []
dfs([1,2,3], 0, res)
print(res)