class Solution:
    def merge(self, intervals):
        intervals.sort(key=lambda i: i[0])
        start, end = intervals[0]
        ans = []
        for i in range(1, len(intervals)):
            if end >= intervals[i][0]:
                end = max(intervals[i][1], end)
            else:
                ans.append([start, end])
                start, end = intervals[i]
        ans.append([start, end])
        return ans
