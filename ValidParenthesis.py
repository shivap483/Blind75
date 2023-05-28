class Solution:
    def isValid(self, s: str) -> bool:
        stack =[]
        opens = ['{','[','(']
        for i in s:
            if i in opens:
                stack.append(i)
            elif len(stack) == 0 or not self.isMatch(stack.pop(), i):
                    return False
        if len(stack) > 0:
            return False
        return True


    def isMatch(self, open, close):
        if open == "[" and close == "]" or open == "{" and close == "}" or open == "(" and close == ")":
            return True
        return False