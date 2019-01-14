arr2d = [[1,  2,  3],
         [4,  5,  6],
         [7,  8,  9]]

arr2d = [[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]]


def edge_print(arr2d, min_row, min_col, max_row, max_col):
    '''
    * * * * *
    '''
    if min_row == max_row:
        for col in range(min_col, max_col + 1):
            print(arr2d[min_row][col])
        return

    '''
    *
    *
    *
    *
    '''
    if min_col == max_col:
        for row in range(min_row, max_row + 1):
            print(arr2d[row][min_col])
        return
    
    '''         
    |* * * *|*| 
    |*|* * *|*|
    |*|* * *|*|
    |*|* * * *|
     '''

    for col in range(min_col, max_col):
        print(arr2d[min_row][col])
    for row in range(min_row, max_row):
        print(arr2d[row][max_col])
    for col in range(max_col, min_col, -1):
        print(arr2d[max_row][col])
    for row in range(max_row, min_row, -1):
        print(arr2d[row][min_col])


#edge_print(arr2d, 0, 0, 3, 2)

def spiral_print(arr2d):
    if not arr2d:
        return
   
    n_rows = len(arr2d)
    if n_rows == 0:
        return
    n_cols = len(arr2d[0])

    min_row, min_col = 0, 0
    max_row, max_col = n_rows - 1, n_cols - 1
    while min_row <= max_row and min_col <= max_col:
        edge_print(arr2d, min_row, min_col, max_row, max_col)
        min_col += 1
        min_row += 1
        max_col -= 1
        max_row -= 1

spiral_print(arr2d)


