class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) % 2 !=0 or len(s) < 2:
            return False

        match = {"}": "{","]": "[", ")": "("}
        # create stack
        # if the character is an opening one push it into the
        # stack. If not, check of the last of the stack (LIFO)
        # equals c, if yes drop the last element of the stack, 
        # if not return False

        stack = []

        for c in s:
            if c in ["}", "]", ")"]:
                if stack and match[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
            print(stack)

        return True if not stack else False


