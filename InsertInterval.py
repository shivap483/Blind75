class Solution:
    def insert(self, intervals, newInterval):
        ans = []
        i = 0
        n = len(intervals)
        while i < n and intervals[i][1] < newInterval[0]:
            ans.append(intervals[i])
            i += 1

        while i < n and not intervals[i][0] > newInterval[1]:
            newInterval = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])]
            i += 1
        ans.append(newInterval)

        while i < n:
            ans.append(intervals[i])
            i += 1
        return ans