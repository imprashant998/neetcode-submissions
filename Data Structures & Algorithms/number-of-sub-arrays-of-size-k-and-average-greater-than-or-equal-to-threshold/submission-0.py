class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        L = 0
        R = k
        result = 0
        while R <= len(arr):
            avg = sum(arr[L:R])/k
            if avg >= threshold:
                result +=1
            L +=1
            R +=1
        return result


        