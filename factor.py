def dfs(arr, start, curr_res, res, target):
    if target == 1:
        res.append(curr_res[:])
        return

    
    for i in range(start, target + 1):
        if target % i == 0:
            curr_res.append(i)
            dfs(arr, i, curr_res, res, target // i)
            curr_res.pop()




arr = [1,2,3]
res = []
dfs(arr, 2, [], res, 18)        
print(res)