class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue1 = []
        self.queue2 = []
        

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.queue1.append(x)
        

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        if len(self.queue1) >= 1:
            while len(self.queue1) > 1:
                head = self.queue1[0]
                del self.queue1[0]
                self.queue2.append(head)
            res = self.queue1[0]
            del self.queue1[0]
            self.queue1, self.queue2 = self.queue2, self.queue1
            return res

            
    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        if len(self.queue1) >= 1:
            while len(self.queue1) > 1:
                head = self.queue1[0]
                del self.queue1[0]
                self.queue2.append(head)
            res = self.queue1.pop()
            #-------------至此 queue1 是空的----------------
            self.queue2.append(res)
            # 交换，保证 queue2 是空的
            self.queue1, self.queue2 = self.queue2, self.queue1
            return res

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return len(self.queue1) == 0
        


# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(2)
obj.push(1)
print(obj.queue1)
print(obj.queue2)
obj.top()
print(obj.queue1)
print(obj.queue2)
param_2 = obj.pop()
param_3 = obj.pop()
param_4 = obj.empty()
print(param_4)

