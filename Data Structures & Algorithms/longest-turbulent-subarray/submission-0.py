class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) < 2:
            return len(arr)
        result = 1
        count = 1
        prev_sign = ""
        for i in range(1,len(arr)):
            if arr[i-1] < arr[i]:
                count = count +1 if prev_sign == ">" else 2
                prev_sign = "<"
            elif arr[i-1] > arr[i]:
                count = count +1 if prev_sign == "<" else 2
                prev_sign = ">"
            else:
                count = 1
                prev_sign = "="
            result = max(result, count)
        return result

        