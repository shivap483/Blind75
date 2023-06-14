class Solution:
    def rob(self, nums):
        rob1, rob2 = 0, 0
        for num in nums:
            temp = max(rob1 + num, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2

    # decision:
    #       If I take current index house, then the amount I can collect would be value at current + max of value from current + 2 sub array.
    #       If I don't take current index house, then the amout I can collect would be max of value max of value from current + 1 sub array

    # n = len(nums)
    # visited = {}

    # def get_max(i):
    #     if i >= n:
    #         return 0
    #     if i not in visited:
    #         visited[i] = max(nums[i] + get_max(i + 2), get_max(i + 1))
    #     return visited[i]

    # return get_max(0)
