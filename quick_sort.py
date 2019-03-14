from random import randint

def partition(arr, l, r):
    '''
    ... * * * * * ...
        l       r
        i         j
    arr[l, i] <= pivot
    arr[i+1, j-1] to be considered
    arr[j, r] > pivot
    '''
    i = l
    j = r + 1
    
    rd = randint(l, r)
    arr[l], arr[rd] = arr[rd], arr[l]
    pivot = arr[l]
    
    while i + 1  <= j - 1:
        if arr[i + 1] <= pivot:
            i += 1
        else:
            arr[i + 1], arr[j - 1] = arr[j - 1], arr[i + 1]
            j -= 1
    
    arr[l], arr[i] = arr[i], arr[l]
    
    return i
    
def quick_sort(arr, l, r):
    if l >= r:
        return
    
    p = partition(arr, l, r)
    quick_sort(arr, l, p - 1)
    quick_sort(arr, p + 1, r)
    
arr = [randint(1, 100) for i in range(20)]
print(arr)
quick_sort(arr, 0, len(arr) - 1)
print(arr)
