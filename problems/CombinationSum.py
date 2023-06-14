class Solution:
    def combinationSum(self, candidates , target: int):
        ans = []
        temp = []
        self.findCombinations(candidates, target, ans, temp, i=0)
        return ans

    def findCombinations(self, candidates, target, ans, temp, i):
        if i == len(candidates):
            if target == 0:
                ans.append(temp.copy())
            return

        if candidates[i] <= target:
            temp.append(candidates[i])
            self.findCombinations(candidates, target - candidates[i], ans, temp, i)
            temp.pop()
        self.findCombinations(candidates, target, ans, temp, i + 1)