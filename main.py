class MyGrid:

    def __init__(self, row, col, dist):
        self.row = row
        self.col = col
        self.dist = dist


def validNode(x, y, grid, visited):
    if ((x >= 0 and y >= 0) and
            (x < len(grid) and y < len(grid[0])) and
            (grid[x][y] != '0') and (visited[x][y] == False)):
        return True
    return False

def minDistance(grid):

    source = MyGrid(0, 0, 0)
    for row in range(len(grid)):
        for col in range(len(grid[row])):
            if grid[row][col] == 'A':
                source.row = row
                source.col = col
                break

    # We are setting all nodes in visited queue as false
    visited = [[False for k in range(len(grid[0]))]
               for l in range(len(grid))]

    # applying BFS on all nodes starting from source
    queue = []
    queue.append(source)
    visited[source.row][source.col] = True
    while len(queue) != 0:
        source = queue.pop(0)

        if (grid[source.row][source.col] == 'B'):
            return source.dist

        # checking the neighbour nodes if it is valid or not
        if validNode(source.row - 1, source.col, grid, visited):
            queue.append(MyGrid(source.row - 1, source.col, source.dist + 1))
            visited[source.row - 1][source.col] = True

        if validNode(source.row + 1, source.col, grid, visited):
            queue.append(MyGrid(source.row + 1, source.col, source.dist + 1))
            visited[source.row + 1][source.col] = True

        if validNode(source.row, source.col - 1, grid, visited):
            queue.append(MyGrid(source.row, source.col - 1, source.dist + 1))
            visited[source.row][source.col - 1] = True

        if validNode(source.row, source.col + 1, grid, visited):
            queue.append(MyGrid(source.row, source.col + 1, source.dist + 1))
            visited[source.row][source.col + 1] = True

    return -1


print("Program to find Shortest distance from A to B in a 2D Grid")

R = int(input("Enter the number of rows:"))
C = int(input("Enter the number of columns:"))


matrix = []
print("Enter the entries row wise as 0,1:")

for i in range(R):
    a = []
    for j in range(C):
        a.append(input())
    matrix.append(a)

print("Layout of the entered Grid is")
for i in range(R):
    for j in range(C):
        print(matrix[i][j], end = " ")
    print()

if minDistance(matrix) < 0:
    print("There is no path from A to B")
else: print("The shortest distance from A is",minDistance(matrix))


