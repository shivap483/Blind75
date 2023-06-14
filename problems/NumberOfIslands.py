import collections


class Solution:
    def numIslands(self, grid):
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        islands = 0
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def set_zeros(r, c):
            if r in range(rows) and c in range(cols) and grid[r][c] == "1":
                grid[r][c] = "0"
                for dr, dc in directions:
                    set_zeros(r + dr, c + dc)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    set_zeros(r, c)
                    islands += 1
        return islands

        # if not grid:
        #     return 0

        # rows, cols = len(grid), len(grid[0])
        # visited = set()
        # islands = 0

        # def bfs(r, c):
        #     q = collections.deque()
        #     visited.add((r, c))
        #     q.append((r, c))

        #     while q:
        #         row, col = q.popleft()
        #         directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        #         for dr, dc in directions:
        #             r = row + dr
        #             c = col + dc
        #             if (
        #                 r in range(rows)
        #                 and c in range(cols)
        #                 and grid[r][c] == "1"
        #                 and (r, c) not in visited
        #             ):
        #                 visited.add((r, c))
        #                 q.append((r, c))

        # for r in range(rows):
        #     for c in range(cols):
        #         if grid[r][c] == "1" and (r, c) not in visited:
        #             islands += 1
        #             bfs(r, c)
        # return islands
