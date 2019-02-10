def dfs(ip, level, curr_res, res):
    if len(curr_res) > 4 or level > len(ip):
        return
    if len(curr_res) == 4 and level == len(ip):
        res.append('.'.join(curr_res))
        return

    for i in range(1, 4):
        if level + i > len(ip):
            break
        num = ip[level: level + i]
        curr_res.append(num)
        if (len(num) > 1 and int(num[0]) != 0 and int(num) <= 255) or (len(num) == 1):
            dfs(ip, level + i, curr_res, res)
        curr_res.pop()
    

res = []
dfs('1921681151', 0, [], res)
print(res)
    