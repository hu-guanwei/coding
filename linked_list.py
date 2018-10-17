#增删改查

class Node(object):
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node

    def print_val(self):
        return self.val
    
    def print_all_after(self):
        while self is not None:
            print(self.val, end=' -> ')
            self = self.next
        print('None')

def search_by_index(head, index):
    cnt = 0
    # stop when cnt == index
    # then do not go further
    while cnt < index:
        if head is None:
            return None
        else:
            head = head.next
            cnt += 1
    return head

def search_by_val(head, val):
    if head is None:
        return None
    while head is not None:
        if head.val == val:
            return head
        else:
            head = head.next

def insert(head, index, val):
    if index < 0:
        return head
    dummy_head = Node(0)
    dummy_head.next = head
    prev = search_by_index(dummy_head, (index - 1) + 1)
    new_node = Node(val)
    new_node.next = prev.next
    prev.next = new_node
    return dummy_head.next

def remove(head, index):
    if index < 0:
        return head
    dummy_head = Node(0)
    dummy_head.next = head
    prev = search_by_index(dummy_head, index - 1 + 1)
    prev.next = prev.next.next
    return dummy_head.next

node_5 = Node(5)
node_4 = Node(4, node_5)
node_3 = Node(3, node_4)
node_2 = Node(2, node_3)
node_1 = Node(1, node_2)

node_1.print_all_after()    
# 头部插入测试
new_head = insert(head=node_1, index=0, val=0)
new_head.print_all_after()
# 尾部插入测试
new_head = insert(head=new_head, index=6, val=6)
new_head.print_all_after()
# 中部插入测试
new_head = insert(head=new_head, index=3, val=1000)
new_head.print_all_after()

# 删除测试
new_head = remove(head=new_head, index=3)
new_head.print_all_after()

#print(search_by_index(node_1, 3).print_val())
#print(search_by_index(node_1, 100))
#print(search_by_val(node_1, 5).print_val())
