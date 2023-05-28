class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        c = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                c[j] += c[j - 1]
        return c[-1]