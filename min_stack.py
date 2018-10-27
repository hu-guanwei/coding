#leetcode 155
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self._items = []
        self._curr_min = []

    def empty(self):
        return len(self._items) == 0
    
    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if not self.empty():
            self._curr_min.append(min(self._curr_min[-1], x))
        else:
            self._curr_min.append(x)
        self._items.append(x)

    def pop(self):
        """
        :rtype: void
        """
        if not self.empty():
            self._items.pop()
            self._curr_min.pop()
        

    def top(self):
        """
        :rtype: int
        """
        if not self.empty():
            return self._items[-1]
        return None

    def getMin(self):
        """
        :rtype: int
        """
        if not self.empty():
            return self._curr_min[-1]
        return None


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()