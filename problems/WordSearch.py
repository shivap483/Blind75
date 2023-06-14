class Solution:
    def exist(self, board, word: str) -> bool:
        points= []
        ans = False
        path = set()
        def dfs(r, c, i):
            if i == len(word):
                return True
            if not (0 <= r < len(board)) or not (0 <= c < len(board[0])) or word[i] != board[r][c] or (r,c) in path:
                return False
            path.add((r,c))
            res = dfs(r, c - 1, i + 1) or dfs(r, c + 1, i + 1) or dfs(r - 1, c, i + 1) or dfs(r + 1, c, i + 1)
            path.remove((r,c))
            return res
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == word[0]:
                    points.append((r,c))
        for r, c in points:
            ans = ans or dfs(r, c, 0)
            if ans:
                return True
        return ans
            
