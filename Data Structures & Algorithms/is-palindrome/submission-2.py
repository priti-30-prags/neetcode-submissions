class Solution:
    def isPalindrome(self, s: str) -> bool:
        m= len(s)//2
        left = 0
        right = -1
        while left<=m:
            if s[left].isalnum():
                if s[right].isalnum():
                    if s[right]==s[left]  or s[right].upper() == s[left].upper():
                        right = right - 1
                        left = left + 1
                    else:
                        return False
                else:
                    right = right - 1
            else:
                left = left + 1
        return True