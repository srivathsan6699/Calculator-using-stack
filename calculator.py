import sys
expression = sys.argv[-1]
operators = set(['+', '-', '*', '/'])
priority = {'+': 1, '-': 1, '*': 2, '/': 2}
def infixtopostfix(expression):
    stack = []
    output = ''
    for ch in expression:
        if ch not in operators:
            output += ch
        else:
            while stack and stack[-1] and priority[ch] <= priority[stack[-1]]:
                output += stack.pop()
            stack.append(ch)
    while stack:
        output += stack.pop()
    return output
expression = input()
def evaluate_postfix(expressions):
    stack = []
    for i in expressions:
        if i not in operators:
            stack.append(i)
        else:
            a = stack.pop()
            b = stack.pop()
            if i == '+':
                result = int(b) + int(a)
            elif i == '-':
                result = int(b) - int(a)
            elif i == '*':
                result = int(b) * int(a)
            elif i == '/':
                result = int(b) / int(a)
            stack.append(result)
    return (''.join(map(str, stack)))
expressions = (infixtopostfix(expression))
print('Your result is : ', evaluate_postfix(expressions))

