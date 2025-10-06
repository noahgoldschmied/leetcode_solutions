class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        c = set()
        res = 0
        l = 0

        for r in range(len(s)):
            while s[r] in c:
                c.remove(s[l])
                l += 1
            c.add(s[r])
            res = max(res, r - l + 1)

        return res
