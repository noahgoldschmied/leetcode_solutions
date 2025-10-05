class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        vals = []
        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] += 1

        for num, count in freq.items():
            vals.append([count, num])
        vals.sort()

        res = []
        while len(res) < k:
            res.append(vals.pop()[1])
        return res
        

        