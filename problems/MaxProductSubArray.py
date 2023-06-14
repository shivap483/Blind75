class Solution:
    def maxProduct(self, nums):
        ans = max(nums)
        cur_max, cur_min = 1, 1
        for num in nums:
            temp = cur_max * num
            cur_max = max(temp, cur_min * num, num)
            cur_min = min(temp, cur_min * num, num)
            ans = max(ans, cur_max)
        return ans
