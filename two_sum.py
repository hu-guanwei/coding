arr = [1, 3, 5, 6, 8, 10, 7, 6, 2, 3, 4, 2, 0, 1]

def two_sum(arr, target):
    '''
    given a array and a number: target
    print all combinations of elements in the array
    that sum up to target
    '''
    seen = set()
    for this_num in arr:
        other_num = target - this_num
        if other_num in seen:
            print(this_num, other_num)
         else:
            seen.add(this_num)

def two_sum_index(arr, target):
    d = dict()
    for index, ele in enumerate(arr):
        if ele not in d:
            d[target - ele] = index
        else:
            print(index, d[ele])
            
two_sum(arr, 11)
print('-'*10)
two_sum_index(arr, 11)
