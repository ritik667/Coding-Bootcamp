def evaluate1(s):
    nums=[]
    symbol = []
    precedence = {'+':1, '-':1, '*':2, '/':2}
    i = 0
    while i < len(s):
        if s[i].isdigit():
            num = ''
            while i < len(s) and s[i].isdigit():
                num += s[i]
                i += 1
            nums.append(int(num))
        else: 
            while(symbol and precedence[symbol[-1]] >= precedence[s[i]]):
                op = symbol.pop()
                num2 = nums.pop()
                num1 = nums.pop()
                if op == '+':
                    nums.append(num1 + num2)
                elif op == '-':
                    nums.append(num1 - num2)
                elif op == '*':
                    nums.append(num1 * num2)
                elif op == '/':
                    nums.append(num1 // num2)
            symbol.append(s[i])
            i += 1
    while symbol:
        op = symbol.pop()
        num2 = nums.pop()
        num1 = nums.pop()
        if op == '+':
            nums.append(num1 + num2)    
        elif op == '-':
            nums.append(num1 - num2)
        elif op == '*':
            nums.append(num1 * num2)
        elif op == '/':
            nums.append(num1 // num2)
    res = nums.pop()
    return res

s = "8/2+4/3*7"
print(evaluate1(s))