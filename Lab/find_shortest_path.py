from collections import deque

#Question: Given a 2D grid where 0s represent empty spaces and 1s represent obstacles,
#write a function to find the shortest path
#from the top-left corner to the bottom-right corner.
#You can move only right or down.

def shortest_path(grid):
    """find shortest path length"""
    
    rows = len(grid)    #length of rows
    cols = len(grid[0]) #length of columns
    
    directions = [(0, 1), (1, 0)]   #Directions for moving right and down
    queue = deque([(0, 0, 0)])      #row, col, distance
    visited = set((0, 0))           #Set of visited point

    #If these positions are 1, path cannot be found
    if grid[0][0] == 1 or grid[rows - 1][cols - 1] == 1:
        return -1
    
    while queue:
        #Pop left queue to find a new way from here
        row, col, dist = queue.popleft()

        #If reached the bottom-right corner, return distance
        if row == rows - 1 and col == cols - 1:
            return dist

        #Explore neighbors
        for dr, dc in directions:
            nr = row + dr
            nc = col + dc
            if (0 <= nr and nr < rows) and (0 <= nc and nc < cols) and grid[nr][nc] == 0 and (nr, nc) not in visited:
                visited.add((nr, nc))
                queue.append((nr, nc, dist + 1))
    #If queue is exhausted without finding the bottom-right corner
    return -1

if __name__ == '__main__':
    grid = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    print(shortest_path(grid))  # Output: 4