class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res, left, right = 0, 0, 1
        while right < len(prices):
            if prices[left] < prices[right]:
                res = max(res, prices[right]-prices[left])
            else:
                left = right
            right += 1
        return res