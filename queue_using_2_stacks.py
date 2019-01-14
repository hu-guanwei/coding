class queue(object):
    def __init__(self):
        self.data = []
        self.buffer = []

    
    def push(self, item):
        self.data.append(item)
    

    def pop(self):
        '''
        除了要返回的元素，其他的被倒两次顺序不变
        '''
        if len(self.data) == 0:
            return
    
        # 1st pour
        while len(self.data) > 1:
            self.buffer.append(self.data.pop())
        left_one = self.data.pop()
        # 2nd pour
        while len(self.buffer) > 0:
            self.data.append(self.buffer.pop())
        
        return left_one

    
q = queue()
for i in range(10):
    q.push(i)

for i in range(10):
    print(q.pop())