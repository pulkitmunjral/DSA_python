'''You are given an N*M binary matrix, considering for every 0-cell(cell with value = 0) the distance from this cell to its nearest 1-cell(cell with value = 1) is 'di', you need to find the maximum value of 'di' among all values of 'di'. Formally, if the minimum distance from an 'ith' 0-cell to any 1-cell is ‘di’, you need to find max(di), where i belongs to the set of all 0-cells in the matrix.
Distance between cells (i,j) and (a,b) is given as (|i-a| + |j-b|) i.e the manhattan distance is considered here.
'''

def max01(array):

    ones = []
    rows = len(array)
    cols = len(array[0])
    for i in range(rows):
        for j in range(cols):
            if array[i][j]==1:
                ones.append((i,j))
    len_ones = len(ones)
    if len_ones == rows*cols or len_ones == 0:
        return -1

    ans = 0

    for i in range(rows):
        for j in range(cols):
            if not array[i][j]:
                temp = 10**9

                for k in range(len_ones):
                    temp = min(temp, abs(ones[k][0]-i) + abs(ones[k][1]-j))

                ans = max(temp, ans)
    return ans


arr = [[1,1,1],[0,1,0],[0,0,0]]
print(max01(arr))