class Solution:
    def longestPalindrome(self, s: str) -> str:
        size = len(s)
        max_len = float('-inf')
        ans =""
        for i in range(size):
            # odd length palindromes
            left, right = i,i
            while left >= 0 and right < size and s[left] == s[right]:
                if right - left + 1 > max_len:
                    max_len = right - left + 1
                    ans = s[left: right + 1]
                left -= 1
                right += 1

            # even length palindromes
            left, right = i, i+1
            while left >= 0 and right < size and s[left] == s[right]:
                if right - left +1 > max_len:
                    max_len = right - left + 1
                    ans = s[left: right + 1]
                left -= 1
                right += 1
        return ans



