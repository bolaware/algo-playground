def balance_parentheses(s: str) -> bool:
    stack = []
    closed_brackets = {')', '}', ']'}
    for char in s:
        if char not in closed_brackets:
            stack.append(char)
        else:
            last = stack.pop()
            if char == ')':
                if last != "(":
                    return False
            elif char == '}':
                if last != "{":
                    return False
            else:
                if last != "[":
                    return False
    return stack == []

print(balance_parentheses("()"))
print(balance_parentheses("()[]{}"))
print(balance_parentheses("(]"))

