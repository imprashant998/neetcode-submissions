class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        curr_sum = 0
        max_sum_linear = nums[0]
        min_sum_linear = nums[0]
        for num in nums:
            if curr_sum < 0 :
                curr_sum = num
            else:
                curr_sum += num
            max_sum_linear = max(max_sum_linear,curr_sum)
        if max_sum_linear < 0:
            return max_sum_linear # Edge case: 
                                # If all numbers are negative, total - min would give you an empty subarray (which is invalid). 
                                # So you need to check if globMax > 0 before considering the circular case.
        for num in nums:
            if curr_sum >0:
                curr_sum = num
            else:
                curr_sum += num
            min_sum_linear = min(min_sum_linear,curr_sum)
        return max(max_sum_linear, sum(nums)-min_sum_linear)
        

        