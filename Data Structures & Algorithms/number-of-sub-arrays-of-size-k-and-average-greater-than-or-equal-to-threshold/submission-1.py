class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        L = 0
        R = k-1
        result = 0 
        sum_ = sum(arr[L:R]) # first window but the last element
        while R < len(arr):
            sum_ += arr[R] # window sum
            if sum_/k >= threshold:
                result +=1
            sum_ -= arr[L]
            L +=1
            R +=1
        return result

        # the only difference is instead of keep using sum(), we are reusing the partial sum of the prev window


        