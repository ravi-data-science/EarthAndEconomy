class Solution:
    def isValid(self, s: str) -> bool:
        Map = {")": "(", "]": "[", "}": "{"}
        stack = []

        for c in s:
            if c not in Map:
                stack.append(c)
                continue
            if not stack or stack[-1] != Map[c]:
                return False
            stack.pop()

        return not stack
    
    def isValid_simple(self, s: str) -> bool:
        stack = []
        closeToOpenMap = {")":"(","[":"[","}":"{"}

        for c in s:
            if c in closeToOpenMap:
                if stack and stack[-1] == closeToOpenMap[c]:
                   stack.pop()
                else:
                    return False
            else:
                stack.append(c) 
        return True if not stack else False

    
if __name__ == '__main__':

    cla1 = Solution()
    isVal = cla1.isValid('[]{}') 
    print(isVal)

    isVal = cla1.isValid('[{}') 
    print(isVal)