class Solution:
    def isPalindrome(self, s: str) -> bool:
        L = 0
        R = len(s)-1
        while L < R:
            while L < R and not s[L].isalnum():
                L +=1
            while L < R and not s[R].isalnum():
                R -=1
            # the above two inner while loop skips non -alphanumeric chars
            if s[L].lower() != s[R].lower():
                return False
            R -=1
            L +=1
        return True
        