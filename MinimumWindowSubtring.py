class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tl = len(t)
        sl = len(s)
        if tl == 0 or tl > sl:
            return ""
        have, need = {}, {}
        for c in t:
            need[c] = 1 + need.get(c, 0)

        have_count, need_count = 0, len(need)
        res = [-1, -1]
        min_length = float('inf')
        l = 0

        for r in range(sl):
            c = s[r]
            have[c] = 1 + have.get(c, 0)
            if c in need and need[c] == have[c]:
                have_count += 1

            while have_count == need_count:
                if r - l + 1 < min_length:
                    res = [l, r]
                    min_length = r - l + 1
                c = s[l]
                have[c] -= 1
                if c in need and have[c] < need[c]:
                    have_count -= 1
                l += 1

        if min_length > len(s):
            return ""
        l, r = res
        return s[l: r + 1]
