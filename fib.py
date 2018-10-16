class Solution(object):
    def fib(self, n):
        if n == 0:
            return 0
        elif n == 1:
            return 1

        '''
        index: 0 1 2 3 4 5 6 7
        value: a b
                 a b
                   a b
                     a b
                       a b
                         a b
                           a b
        '''
        a, b = 0, 1
        for i in range(n - 1):
            a, b = b, a + b
        return b

assert(Solution().fib(0) == 0)
assert(Solution().fib(1) == 1)
assert(Solution().fib(2) == 1)
assert(Solution().fib(3) == 2)
assert(Solution().fib(4) == 3)
assert(Solution().fib(5) == 5)
assert(Solution().fib(6) == 8)
assert(Solution().fib(7) == 13)
assert(Solution().fib(8) == 21)
assert(Solution().fib(9) == 34)
