Class Solution(object):
    def isValid(self, s):
        stack = []
        brackets = {')':'(', '}':'{', ']':'['}
        for i in s:
            if i in brackets.values():
                stack.append(i)
            elif i in brackets.keys():
                if stack == [] or brackets[i] != stack.pop():
                    return False
                else:
                    return True
        return stack == []
        
                    
        
        
            