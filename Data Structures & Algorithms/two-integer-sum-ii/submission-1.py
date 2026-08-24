class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        L = 0
        R = len(numbers) - 1
        while L < R:
            total = numbers[L] + numbers[R]
            if total == target:
                return [L+1,R+1]
            elif total < target:
                # we need to update the left pointer to make it point to a larger integer
                L +=1
            else:
                R -=1
        # there is always one solution, so while loop must return early.
            
