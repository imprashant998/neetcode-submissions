class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        L = 0
        length = float("inf")
        sum_ = 0
        for R in range(len(nums)):
            sum_ += nums[R]
            while sum_ >= target:
                length = min(length, R-L+1)
                sum_ -= nums[L]
                L +=1
        return 0 if length == float("inf") else length

