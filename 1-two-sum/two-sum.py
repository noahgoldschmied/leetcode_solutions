class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sol = {}
        idx = 0
        for num in nums:
            diff = target - num
            if diff in sol:
                return [sol[diff], idx]
            sol[num] = idx
            idx += 1
        