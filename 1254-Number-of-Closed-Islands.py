class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def dfs(r: int, c: int) -> bool:
            # If we go out of bounds, it means this island touches the border
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return False
            # If it's water (1) or already visited (marked as 1), it doesn't violate closedness
            if grid[r][c] == 1:
                return True

            # Mark land as visited by converting it to water (1)
            grid[r][c] = 1

            # Traverse all 4 directions
            # Note: Avoid short-circuiting with `and` by computing each call
            up = dfs(r - 1, c)
            down = dfs(r + 1, c)
            left = dfs(r, c - 1)
            right = dfs(r, c + 1)

            return up and down and left and right

        closed_count = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    if dfs(r, c):
                        closed_count += 1

        return closed_count