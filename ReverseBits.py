class Solution:
    def reverseBits(self, n):
        ans = 0
        while n > 0:
            bit = n >> 1 & 1
            ans = ans << 1 | bit
            n = n >> 1
        return ans
