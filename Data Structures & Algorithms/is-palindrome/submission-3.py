class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while left < right:
            if s[left].isalnum():
                if s[right].isalnum():
                    if s[right]==s[left]  or s[right].lower() == s[left].lower():
                        right = right - 1
                        left = left + 1
                    else:
                        return False
                else:
                    right = right - 1
            else:
                left = left + 1
        return True