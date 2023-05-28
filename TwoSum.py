from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        map = {}
        for i, num in enumerate(nums):
            if num in map:
               return [map[num], i]
            else:
                map[target-num] = i
