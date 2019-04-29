def lcs(str1, str2):
    if not str1 or not str2:
        return ''
    if len(str1) == 0 or len(str2) == 0:
        return ''

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
    m, n = len(str1), len(str2)
    table = [[0 for j in range(n + 1)] for i in range(m + 1)]
    end_i = end_j = 0
    M = 0
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            table[i][j] = table[i-1][j-1] + 1 if str1[i-1] == str2[j-1] else 0
            if table[i][j] > M:
                M = table[i][j]
                end_i, end_j = i, j

    if M == 0:
        return ''
    start_i = end_i
    start_j = end_j
    while start_i >= 0 and start_j >= 0 and table[start_i][start_j] > 0 :
        start_i -= 1
        start_j -= 1
    # ~ a p p [start_i + 1, end_i]
    # app[start_i, end_i - 1]
    # app[start_i: end_i]
    return str1[start_i: end_i]


if __name__ == '__main__':
    # test case 1
    assert(lcs('app', 'ppt') == 'pp')
    # test case 2
    assert(lcs('sweden', 'student') == 'den')
    # test case 3
    assert(lcs('aaaaaa', 'bbb') == '')