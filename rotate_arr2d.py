arr2d = [[ 1,  2,  3,  4],
         [ 5,  6,  7,  8],
         [ 9, 10, 11, 12],
         [13, 14, 15, 16]]

def rotate_edge(arr2d, min_row, min_col, max_row, max_col):
    assert(min_row == min_col)
    assert(max_row == max_col)
    
    '''
    |* * *|*|
    |*|* *|*|
    |*|* *|*|
    |*|* * *|
    '''
    for offset in range(0, max_col - min_col):
        temp = arr2d[min_row][min_col + offset]
        arr2d[min_row][min_col + offset] = arr2d[max_row - offset][min_col]
        arr2d[max_row - offset][min_col] = arr2d[max_row][max_col - offset]
        arr2d[max_row][max_col - offset] = arr2d[min_row + offset][max_col] 
        arr2d[min_row + offset][max_col] = temp


def rotate(arr2d):
    n_rows = len(arr2d)
    if n_rows == 0:
        return
    n_cols = len(arr2d[0])
    assert(n_cols == n_rows)
    
    min_row, min_col = 0, 0
    max_row, max_col = n_rows - 1, n_cols - 1
    while max_row >= min_row and max_col >= min_col:
        rotate_edge(arr2d, min_row, min_col, max_row, max_col)
        min_row += 1
        min_col += 1
        max_row -= 1
        max_col -= 1
     

#rotate_edge(arr2d, 0, 0, 3, 3)
rotate(arr2d)
print(arr2d)