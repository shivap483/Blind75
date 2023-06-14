class Solution:
    def findMin(self, nums):
        s = 0
        e = len(nums) - 1
        ans = float("inf")
        while s <= e:
            mid = s + (e - s) // 2
            ans = min(ans, nums[mid])
            if ans < nums[e]:
                e = mid - 1
            else:
                s = mid + 1
        return ans
