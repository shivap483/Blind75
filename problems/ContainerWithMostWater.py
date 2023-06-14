from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        ans = 0
        while left < right:
            cur_area = (right - left) * min(height[left], height[right])
            ans = max(cur_area, ans)
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return ans

