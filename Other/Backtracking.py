# find the shortest path to reach a target and return step
inf = 10 ** 9


def move(grid, visited, x, y, targetX, targetY, m, n):
    if x >= m or y >= n or x < 0 or y < 0 or grid[x][y] == 0 or visited[x][y] == 1:
        return inf

    if x == targetX and y == targetY:
        return 1
    visited[x][y] = 1
    moveRight = move(grid, visited, x, y + 1, targetX, targetY, m, n)
    moveDown = move(grid, visited, x + 1, y, targetX, targetY, m, n)
    moveLeft = move(grid, visited, x, y - 1, targetX, targetY, m, n)
    moveUp = move(grid, visited, x - 1, y, targetX, targetY, m, n)
    visited[x][y] = 0
    return 1 + min(moveRight, moveLeft, moveUp, moveDown)


grid = [[0, 1, 0],
        [0, 0, 1],
        [1, 1, 1]]

visited = [[False for _ in range(3)] for _ in range(3)]
print(move(grid, visited, 2, 0, 1, 1, 3, 3))

