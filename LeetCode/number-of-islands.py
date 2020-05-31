class Solution(object):
    
    
    def exploreIsland(self, visited, grid, stack):
        while len(stack) != 0:
            row,col = stack.pop()
            if row - 1 >= 0 and not visited[row-1][col] and grid[row - 1][col] == '1':
                stack.append((row-1,col))
                visited[row - 1][col] = True
            if col - 1 >= 0 and not visited[row][col - 1] and grid[row][col - 1] == '1':
                stack.append((row,col - 1))
                visited[row][col - 1] = True
            if row + 1 < len(visited) and not visited[row + 1][col] and grid[row + 1][col] == '1':
                stack.append((row + 1,col))
                visited[row + 1][col] = True
            if col + 1 < len(visited[0]) and not visited[row][col + 1] and grid[row][col + 1] == '1':
                stack.append((row,col + 1))
                visited[row][col + 1] = True
                    
        return visited
                
    
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        islandCount = 0 
        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        visited = [[False for j in range(len(grid[0]))]for i in range(len(grid))]

        for col in range(len(grid[0])):
            for row in range(len(grid)):
                if not visited[row][col] and grid[row][col] == '1':
                    stack = [(row,col)]
                    visited[row][col] = True
                    visited = self.exploreIsland(visited, grid, stack)
                    islandCount += 1
                visited[row][col] = True
        
        return islandCount 
        