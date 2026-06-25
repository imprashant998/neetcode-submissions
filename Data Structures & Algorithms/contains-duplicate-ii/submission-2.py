class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # brute force
        l = 0
        # r = k, if k is greater than len(nums) it shall be out of index
        r = min(k,len(nums)-1)
        while r < len(nums):
            for curr in range(l+1,r+1):
                if nums[l] == nums[curr]:
                    return True
            l +=1
            r +=1
        return False

        