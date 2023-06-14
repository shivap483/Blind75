class Solution:
    def setZeroes(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        zeros =[]
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    zeros.append((r, c))

        for row, col in zeros:
            self.set(row, col, matrix)
        return matrix

    def set(self,row, col, matrix):
        for i in range(len(matrix)):
            matrix[i][col] = 0
        for i in range(len(matrix[0])):
            matrix[row][i] = 0
