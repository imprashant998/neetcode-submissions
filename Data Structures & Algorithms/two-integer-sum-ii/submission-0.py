class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        L = 0
        R = len(numbers) -1
        while L < R:
            sum_ = numbers[L] + numbers[R]
            if sum_ < target:
                # we added the largest with the smallest; still falling short, increase the smallest to a larger one
                L +=1
            elif sum_ > target:
                # we added the largest with the smallest; and overshooting, decrease the largest
                R -=1
            else:
                return [L+1, R+1]
