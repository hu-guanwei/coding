def dfs(arr, level, curr_res, res, target):
    if level == len(arr) - 1:
        if target % arr[level] == 0:
            for j in range(target // arr[level]):
                curr_res.append(arr[level])
            res.append(curr_res[:])
            for j in range(target // arr[level]):
                curr_res.pop()
        return

    for i in range(target // arr[level] + 1): # i = 0, ..., target // arr[level] 分出若干个叉
        for j in range(i):
            curr_res.append(arr[level])       # append 共 i 次
        dfs(arr, level + 1, curr_res, res, target - arr[level] * i)
        for j in range(i):
            curr_res.pop()

res = []
arr = [25, 10, 5, 9]
dfs(arr, 0, [], res, 30)
print(res)

