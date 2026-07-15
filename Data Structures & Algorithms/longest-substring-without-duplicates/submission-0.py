class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = set()
        length = 0
        L = 0
        for R in range(len(s)):
            while s[R] in chars:
                chars.remove(s[L])
                L +=1
            # end of this loop, we get a valid window
            chars.add(s[R])
            length = max(length, R-L+1)
        return length


