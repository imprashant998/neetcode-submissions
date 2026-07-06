class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        diff_array = []
        for i in range(len(nums)-1):
            diff = nums[i] - nums[i+1]
            diff_array.append(diff)
        return all(x>=0 for x in diff_array) or all (x<=0 for x in diff_array)
        