class Solution:
    def __init__(self):
        self.visited = []
        self.row = 0
        self.col = 0

    def init_visited(self):
        for _ in range(self.row):
            self.visited.append([0] * self.col)

    def go(self, row, col, grid):
        if self.visited[row][col] == 1 or grid[row][col] == "0":
            return
        else:
            self.visited[row][col] = 1

        if row + 1 < self.row:
            self.go(row + 1, col, grid)
        if row - 1 >= 0:
            self.go(row - 1, col, grid)
        if col + 1 < self.col:
            self.go(row, col + 1, grid)
        if col - 1 >= 0:
            self.go(row, col - 1, grid)

    def numIslands(self, grid: List[List[str]]) -> int:
        self.row = len(grid)
        self.col = len(grid[0])
        self.init_visited()

        island_cnt = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1" and self.visited[row][col] == 0:
                    self.go(row, col, grid)
                    island_cnt += 1

        return island_cnt
