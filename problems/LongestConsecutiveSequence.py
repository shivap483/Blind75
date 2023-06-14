class Solution:
    def longestConsecutive(self, nums):
        if len(nums) == 0:
            return 0
        nums = sorted(list(set(nums)))
        ll = 1
        i = 1
        while i < len(nums):
            isSubSequence = True
            temp = 1
            while isSubSequence and i < len(nums):
                if nums[i] - nums[i - 1] == 1:
                    temp += 1
                    ll = max(ll, temp)
                else:
                    isSubSequence = False
                i += 1

        return ll
