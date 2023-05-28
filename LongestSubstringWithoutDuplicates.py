class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        size = len(s)
        if size <= 1:
            return s
        left, right = 0, 1
        max_len = float('inf')
        seen = set()
        seen.add(s[left])
        ans, cur = float('-inf'), 1
        while right < size:
            if s[right] not in seen:
                seen.add(s[right])
                cur = cur + 1
                right = right + 1
                ans = max(ans, cur)
            else:
                while left < right:
                    seen.remove(s[left])
                    left = left + 1
                    cur = cur - 1
                    if s[right] not in seen:
                        break
        return ans
