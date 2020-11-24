class Solution:
    def isValid(self, s: str) -> bool:
        bMapping= { ")":"(", "}":"{" , "]":"["  }
        stack = []
        for b in s:
            if b in bMapping:
                top_element = stack.pop() if stack else '#'
                if bMapping[b] != top_element:
                    return False
            else:
                stack.append(b)
        return not stack
