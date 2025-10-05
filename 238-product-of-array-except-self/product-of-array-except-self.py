class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pref = [1]*n
        post = [1]*n
        
        for i in range(n):
            if i == 0:
                pref[i] = 1
                post[n-1] = 1
            else:
                pref[i] = pref[i-1] * nums[i-1]
                post[n-i-1] = post[n-i] * nums[n-i]

        answer = []
        for i in range(n):
            answer.append(pref[i]*post[i])
        return answer