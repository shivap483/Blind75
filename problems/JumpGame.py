class Solution:
    def canJump(self, nums):
        max_reachable_index = 0
        for i, steps in enumerate(nums):
            if i > max_reachable_index:
                return False
            max_reachable_index = max(max_reachable_index, i + steps)
        return True

