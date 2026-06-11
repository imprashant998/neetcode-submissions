class Solution:
    def isValid(self, s: str) -> bool:
        open_close_map = {
            '(':')',
            '{':'}',
            '[':']'
        }
        stack = []
        if s[0] not in open_close_map:
            return False
        for paran in s:
            if paran in open_close_map:
                stack.append(paran)
            else:
                if stack:
                    if open_close_map[stack[-1]] == paran:
                        stack.pop()
                    else:
                        return False
        return len(stack) == 0
