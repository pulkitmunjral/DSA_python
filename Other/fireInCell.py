'''You are given a matrix 'MAT' of size ‘N’ * ‘M’, where ‘N’ is the number of rows and ‘M’ is the number of columns. Value ‘0’ in a cell represents that the cell is set on fire initially, (at time t = ‘0’), and the cells which don’t have fire initially have value = ‘1’, and are called safe cells.
If a cell is on fire, then in one second the fire will expand to its adjacent cells (left, right, top, bottom) if they are not already on fire.
You are given the position of a person as integers ‘X’ and ‘Y’ denoting the cell (‘X’, ‘Y’). In one second the person can move from its current cell to any one of its adjacent cells, provided they are not on fire.
You have to determine if the person can move through the matrix to one of the escape cells without burning himself i.e. without going through the fire cells. If it’s possible, return time taken, else return -1.'''

def isValid(x, y, n, m):

    return x < n and y < m

def isEdge(x, y, n, m):

    return (x==0 and y<m-1 and y>0) or (x==n-1 and y<m-1 and y>0) or (y==0 and x<n-1 and y>0) or (y==m-1 and y<n-1 and y>0)


def findLeastTime(mat, start_x, start_y):

    rows = len(mat)
    cols = len(mat[0])

    timeOfFire = [[0 for _ in range(cols)] for _ in range(rows)]
    visited = [[False for _ in range(cols)] for _ in range(rows)]

    q = []

    for i in range(rows):
        for j in range(cols):
            if mat[i][j] == 0:
                q.append((i, j))
                timeOfFire[i][j] = 0
                visited[i][j] = True

    timer = 1
    xx = [0, 1, 0, -1, 0]
    while q:

        size = len(q)
        for _ in range(size):
            current_x, current_y = q.pop(0)

            for i in range(4):
                next_x = current_x + xx[i]
                next_y = current_y + xx[i+1]
                if isValid(next_x, next_y, rows, cols) and visited[next_x][next_y] == False:
                    visited[next_x][next_y] = True
                    timeOfFire[next_x][next_y] = timer
                    q.append((next_x, next_y))

        timer += 1


    possible = False
    timer = 0

    q.append((start_x, start_y))

    while q:

        size = len(q)

        for _ in range(size):

            current_x, current_y = q.pop(0)

            if isEdge(current_x, current_y, rows, cols):
                possible = True
                break

            for i in range(4):
                next_x = current_x + xx[i]
                next_y = current_y + xx[i+1]
                if isValid(next_x, next_y, rows, cols) and mat[next_x][next_y] == 1:
                    if timer + 1 < timeOfFire[next_x][next_y]:
                        q.append((next_x, next_y))
                        mat[next_x][next_y] = 0

        if possible:
            break
        timer += 1

    return timer if possible else -1



ar=[[0, 1, 1, 1],
[1, 0, 1 ,1],
[1, 1, 1 ,1],
[0 ,1, 1, 0]]

print(findLeastTime(ar, 1, 2))
