class stack(object):
    def __init__(self):
        self.data = []
        self.buffer = []


    def push(self, item):
        self.data.append(item)


    def pop(self):
        if not self.data or len(self.data) == 0:
            return

        while len(self.data) > 1:
            self.buffer.append(self.data.pop(0))
        left_one = self.data.pop(0)
        self.data, self.buffer = self.buffer, self.data
        return left_one

s = stack()
for i in range(10):
    s.push(i)

for i in range(10):
    print(s.pop())