def longest_common_substr(str1, str2):
    if not str1 or not str2:
        return 0
    if len(str1) <= 0 or len(str2) <= 0:
        return 0
    '''
    str1 = 'app'
    str2 = 'ppt'
    
    table[i][j] 记录 str1[0, i-1] (前 i 个) 和 str2[0, j-1] （前 j 个）的最长公共子串
    
    table[i][j] = table[i-1][j-1] + 1 if str1[i-1] == str2[j-1]
                  0                   otherwise
       ~ a p p
    ~  0 0 0 0
    p  0 0 1 1
    p  0 0 1 2
    t  0 1 1 0
    '''
    m = len(str1)
    n = len(str2)
    table = [[0 for j in range(n + 1)] for i in range(m + 1)]
    lcs = 0
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            table[i][j] = table[i - 1][j - 1] + 1 if str1[i - 1] == str2[j - 1] else 0
            lcs = max(lcs, table[i][j])
    return lcs


if __name__ == '__main__':
    str1 = 'app'
    str2 = 'ppt'
    res = longest_common_substr(str1, str2)
    print(res)