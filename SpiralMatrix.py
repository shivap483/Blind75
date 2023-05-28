class Solution:
    def spiralOrder(self, matrix):
        left, top = 0, 0
        rows, cols = len(matrix), len(matrix[0])
        right, bottom = len(matrix[0]), len(matrix)
        ans = []
        while len(ans) < rows*cols:
            for i in range(left, right):
                ans.append(matrix[top][i])
            top += 1
            for i in range(top, bottom):
                ans.append(matrix[i][right - 1])
            right -= 1
            if top < bottom:
                for i in range(right - 1, left - 1, -1):
                    ans.append(matrix[bottom - 1][i])
                bottom -= 1
            if left < right:
                for i in range(bottom - 1, top - 1, -1):
                    ans.append(matrix[i][left])
                left += 1
        return ans
