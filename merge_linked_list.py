class Node(object):
    
    def __init__(self, val, next_node=None):
        self.val = val
        self.next = next_node
        
    def print_all_after(self):
        if self is None:
            print(None)
        while self is not None:
            print(self.val, end=' -> ')
            self = self.next
        print('None')
        return


class Solution(object):
    
    def merge(self, head1, head2):
        if head1 is None and head2 is None:
            return None
        elif head1 is None:
            return head2
        elif head2 is None:
            return head1

        # 需要返回新链表节点
        dummy_head = Node(0)
        curr = dummy_head
        while head1 is not None and head2 is not None:
            if head1.val < head2.val:
                curr.next = head1
                head1 = head1.next
                curr = curr.next
            else:
                curr.next = head2
                head2 = head2.next
                curr = curr.next
        if head1 is not None:
            curr.next = head1
        if head2 is not None:
            curr.next = head2

        return dummy_head.next
                
    
node_1 = Node(1)
node_3 = Node(3)
node_5 = Node(5)
node_1.next = node_3
node_3.next = node_5

node_2 = Node(2)
node_4 = Node(4)
node_2.next = node_4
node_1.print_all_after()
node_2.print_all_after()
Solution().merge(node_1, node_2).print_all_after()


