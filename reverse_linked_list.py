# -*- coding:utf-8 -*-

class Node(object):
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node

def print_all_after(head):
    if head is None:
        return
    while head is not None:
        print(head.val)
        print('|')
        head = head.next
    print('None')

node_5 = Node(5)
node_4 = Node(4, node_5)
node_3 = Node(3, node_4)
node_2 = Node(2, node_3)
node_1 = Node(1, node_2)

print_all_after(node_1)
print('-' * 20)
def reverse(head):
    if head is None or head.next is None:
        return head
    next_node = head.next
    new_head = reverse(next_node)
    next_node.next = head
    head.next = None
    return new_head
print_all_after(reverse(node_1))
