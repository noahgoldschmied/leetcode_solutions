class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_chars = [char for char in s if char.isalnum()]
        cleaned_text = "".join(cleaned_chars)

        if len(cleaned_text) == 0 or len(cleaned_text) == 1:
            return True

        left, right = 0, len(cleaned_text)-1
        lower = cleaned_text.lower()
        while left < right:
            if lower[left] != lower[right]:
                return False
            left += 1
            right -= 1
        return True

