class Solution:
    def reverseParentheses(self, s: str) -> str:
        pair = {}
        stack = []
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            elif char == ')':
                j = stack.pop()
                pair[i] = j
                pair[j] = i
                
        res = []
        i = 0
        direction = 1
        
        while i < len(s):
            if s[i] in '()':
                i = pair[i]
                direction = -direction
            else:
                res.append(s[i])
            i += direction
            
        return "".join(res)