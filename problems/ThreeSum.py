
class Solution:
    def threeSum(self, nums):
        size = len(nums)
        nums.sort()
        ans = []
        for i in range(size):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = size - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
                else:
                    ans.append([nums[i], nums[left], nums[right]])
                    while left + 1 < size and nums[left] == nums[left + 1]:
                        left += 1
                    while right - 1 > 0 and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
        return ans






