class Solution:
    def groupAnagrams(self, strs):
        # hashing
        map = {}
        ans = []
        for str in strs:
            s = sorted(str)
            s = tuple(s)
            if s not in map:
                map[s] = []
            map[s].append(str)
        for key in map:
            ans.append(map[key])
        return ans