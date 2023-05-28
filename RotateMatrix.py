class Solution:
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """

        n = len(matrix)
        for r in range((n+1)//2):
            for c in range(n//2):
                temp = matrix[r][c]
                matrix[r][c] = matrix[n-1-r][c]
                matrix[n - 1 - r][c] = matrix[n - 1 - r][n - 1 - c]
                matrix[n - 1 - r][n - 1 - c] = matrix[r][n - 1 - c]
                matrix[r][n - 1 - c] = temp
        return matrix
