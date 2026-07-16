class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        result = 0
        L = 0
        count = dict()
        for R in range(len(s)):
            count[s[R]] = count.get(s[R],0) +1
            maxf = max(count.values())
            # start to shrink when the window is invalid
            while R-L+1 - maxf >k:
                count[s[L]] -=1
                L +=1
                maxf = max(count.values())
            result = max(result,R-L+1)
        return result
            
            