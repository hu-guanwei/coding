import operator

def evalRPN(tokens):
    """
    input: string[] tokens
    return: int
    """
    stack = []
    sign_map = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
	
    for ele in tokens:
        if ele not in ('+', '-', '*', '/'):
            stack.append(ele)
	else:
	    right = int(stack.pop())
	    left = int(stack.pop())
	    sign = sign_map[ele]
	    stack.append(sign(left, right))
    return stack[0]
	
expression = ["2", "1", "+", "3", "*"]
res = evalRPN(expression)
print(res)

#-------------------------------------------------------------------------------------------------------
class Solution(object):
    def evalRPN(self, tokens):
        """
        input: string[] tokens
        return: int
        """
        # write your solution here
        stack = []
        sign_map = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
        for ele in tokens:
            if ele not in sign_map.keys():
                stack.append(ele)
            else:
                right = int(stack.pop())
                left = int(stack.pop())
                sign = sign_map[ele]
                stack.append(sign(left, right))
        return stack[0]
		
assert(Solution().evalRPN(expression) == 9)
assert(Solution().evalRPN(["2", "3", "*", "100", "+"]) == 106)
