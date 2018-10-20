def merge(list1, list2):
    n1 = len(list1)
    n2 = len(list2)
    i = j = 0
    aux = []
    while i < n1 and j < n2:
        if list1[i] < list2[j]:
            aux.append(list1[i])
            i += 1
        else:
            aux.append(list2[j])
            j += 1
    while i < n1:
        aux.append(list1[i])
        i += 1
    while j < n2:
        aux.append(list2[j])
        j += 1
    return aux

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    '''
    mid = (0 + len(arr) - 1) // 2
    left_half = merge_sort(arr[0: mid + 1])
    right_half = merge_sort(arr[mid + 1:])
    '''
    mid = len(arr) // 2
    left_half = merge_sort(arr[0: mid])
    right_half = merge_sort(arr[mid: ])
    return merge(left_half, right_half)

print(merge([1,3,5,7,9], [2,4,6,8,10]))
print(merge([1,2,3,4,5], [1.1,2.2,3.3,4.4,5.5]))
print(merge_sort([10,9,8,7,6,5,4,3,2,1,-100,100]))
