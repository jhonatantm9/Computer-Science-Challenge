class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        def dfs(x, y, visited, total=0):
            total += grid[x][y]
            visited.add((x, y))
            aux = total
            if(x > 0 and grid[x-1][y] != 0):
                if(not (x - 1, y) in visited):
                    total = max(total, dfs(x - 1, y, visited, aux))
            if(y > 0 and grid[x][y-1] != 0):
                if(not (x, y - 1) in visited):
                    total = max(total, dfs(x, y - 1, visited, aux))
            if(x < len(grid) - 1 and grid[x+1][y] != 0):
                if(not (x + 1, y) in visited):
                    total = max(total, dfs(x + 1, y, visited, aux))
            if(y < len(grid[0]) - 1 and grid[x][y+1] != 0):
                if(not (x, y + 1) in visited):
                    total = max(total, dfs(x, y + 1, visited, aux))
            visited.remove((x, y))
            return total
        
        maxGold = 0
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(grid[i][j] != 0):
                    maxGold = max(maxGold, dfs(i, j, visited))
        return maxGold