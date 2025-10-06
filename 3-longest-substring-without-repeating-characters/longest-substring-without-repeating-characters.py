class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res, left, right = 0,0,0
        res_set = set()
        while right < len(s):
            res_set.add(s[right])
            if len(res_set) == right-left+1:
                res = max(res, right-left+1)
                right += 1
            else:
                left +=1
                right = left
                res_set = set()
        return res