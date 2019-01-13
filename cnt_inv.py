def __merge(arr, l, s, r):
    '''
    ... * * * * * ...
        l   s   r
    arr[l, s] sorted
    arr[s+1, r] sorted
    '''
    aux = []
    i = l
    j = s + 1
    cnt_inv = 0
    while i <= s and j <= r:
        if arr[i] < arr[j]:
            aux.append(arr[i])
            i += 1
        else:
            cnt_inv += (s - i + 1)   # arr[j, r] >= arr[i]
            aux.append(arr[j])
            j += 1
    
    while i <= s:
        aux.append(arr[i])
        i += 1

    while j <= r:
        aux.append(arr[j])
        j += 1

    for k in range(l, r + 1):
        arr[k] = aux[k - l]
    
    return cnt_inv

def __merge_sort(arr, l, r):
    if l >= r:
        return 0
    
    m = (l + r) // 2
    cnt_left = __merge_sort(arr, l, m)
    cnt_right = __merge_sort(arr, m + 1, r)
    cnt_split = __merge(arr, l, m, r)
    return cnt_left + cnt_right + cnt_split

def merge_sort(arr):
    return __merge_sort(arr, 0, len(arr) - 1)

n = int(input())
arr = list(map(int, input().strip().split(' ')))
print(merge_sort(arr))