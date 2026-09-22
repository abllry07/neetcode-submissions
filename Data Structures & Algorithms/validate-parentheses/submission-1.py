class Solution:
    def isValid(self, s: str) -> bool:

        # Can create a hash map to map each opening parentheses to its closing one
    
        closeToOpen = { ")" : "(", "]" : "[", "}" : "{"}
        stack = []

        for char in s:
            if char in closeToOpen:
                if stack and stack[-1] == closeToOpen[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        
        return True if not stack else False


        # this code works by first mapping each closing bracket to its opening bracket pair. Then, we go through the input string and add opening parentheses into the stack until we reach our first closing parentheses. Technically, since the opening and closing brackets will end up being at most a position of 1 away from each other, the top of the stack has to be the corresponding closing bracket if the input is valid. this check is repeated until finally, we have no more values in the stack, which is when we return the outcome


        