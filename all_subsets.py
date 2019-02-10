def all_subsets(arr):
    curr_res = []
    res = []
    level = 0
    dfs(arr, curr_res, res, level)
    return res


def dfs(arr, curr_res, res, level):

    if level == len(arr):
        res.append(curr_res[:])
        return

    curr_res.append(arr[level])
    dfs(arr, curr_res, res, level + 1)
    curr_res.pop()

    dfs(arr, curr_res, res, level + 1)
    


arr = [1,2,3,4]

print(all_subsets(arr))