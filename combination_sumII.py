def dfs(arr, level, curr_res, res, target):
    if level == len(arr) - 1:
        if target == arr[level]:
            curr_res(arr[level])
            res.add(tuple(curr_res[:]))
            curr_res.pop()
        if target == 0:
            res.add(tuple(curr_res[:]))
        return

    curr_res.append(arr[level])
    dfs(arr, level + 1, curr_res, res, target - arr[level])
    curr_res.pop()

    dfs(arr, level + 1, curr_res, res, target)   


res = set()
arr = [10,1,2,7,6,1,5]
dfs(sorted((arr)), 0, [], res, 9)
print([list(item) for item in res])
    
        