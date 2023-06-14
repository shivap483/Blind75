class Solution:
    def canFinish(self, numCourses: int, prerequisites):
        map = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            map[crs].append(pre)

        visited = set()

        def dfs(crs):
            if crs in visited:
                return False
            if not map[crs]:
                return True
            visited.add(crs)
            for pre in map[crs]:
                if not dfs(pre):
                    return False
            visited.remove(crs)
            map[crs] = []
            return True

        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True
