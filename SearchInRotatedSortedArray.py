class Solution:
    def search(self, nums, target: int) -> int:
        s = 0
        e = len(nums) - 1
        while s <= e:
            mid = s + (e - s) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] >= nums[s]:
                if nums[s] <= target <= nums[mid]:
                    e = mid - 1
                else:
                    s = mid + 1
            else:
                if nums[mid] <= target <= nums[e]:
                    s = mid + 1
                else:
                    e = mid - 1
        return -1
