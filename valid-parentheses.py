class Solution:
    def isValid(self, s: str) -> bool:
        f={'(': ')', '{': '}', '[': ']'}
        if '{' in s:
            if '}' in s:
                pass
            else:
                return False
        if '[' in s:
            if ']' in s:
                pass
            else:
                return False
        if '(' in s:
            if ')' in s:
                pass
            else:
                return False
        return True

