class Solution:
    def isValid(self, s: str) -> bool:
        # openingParenthesis = ["[", "{", "("]

        pairs = {")" : "(", "]" : "[", "}" : "{"}
        stk = []

        for char in s:
            if char in pairs:
                if not stk or stk[-1] != pairs[char]:
                    return False
                stk.pop()
            else:
                stk.append(char)
        
        return not stk
        



