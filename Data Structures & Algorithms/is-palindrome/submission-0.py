class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(c for c in s if c.isalnum())
        p = s.lower()[::-1]

        if s.lower() == p:
            return True
        else:
            return False