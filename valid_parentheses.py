def is_valid(expression):
    stack = []
    match = {'(': ')', '{': '}', '[': ']'}
    for char in expression:
        # 如果是左括号
        if char in match.keys():
            stack.append(char)
        # 如果是右括号
        elif len(stack) == 0:
            return False
        elif match[stack[-1]] != char:
            return False
        else:
            stack.pop()
    return len(stack) == 0

string = "([])"
res = is_valid([ele for ele in string])

print(res)