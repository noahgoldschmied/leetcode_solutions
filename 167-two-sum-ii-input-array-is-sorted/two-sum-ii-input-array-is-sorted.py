class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        back, front = 0,len(numbers)-1
        while back < front:
            check = numbers[back] + numbers[front]
            if check == target:
                return [back+1, front+1]
            if check > target:
                front -= 1
            else:
                back += 1
        