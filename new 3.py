class ListNode(object):
	def __init__(self, val):
		self.val = val
		self.next = None
	def __eq__(self, other):
		return isinstance(other, ListNode) and self.val == other.val
		
def print_all_nodes(head):
	if head is None:
		return
	while head is not None:
		print(head.val, end=' -> ')
		head = head.next
	print('None')

def print_all_nodes_r(head):
	if head is None:
		print('None')
	else:
		print(head.val, end = ' -> ')
		print_all_nodes_r(head.next)
		
def search_by_index(head, index):
	if head is None or index < 0:
		return None
	for i in range(index):
		head = head.next
		if head is None:
			return None
	return head
	
	
	
def search_by_val(head, val):
	if head is None:
		return None
	while head is not None:
		if head.val = val:
			return head
		else:
			head = head.next
	return None
	
def add(head, index, new_node):
	dummy_head = ListNode(0)
	dummy_head.next = head
	prev = search_by_index(head, index - 1 + 1)
	if prev is None:
		return
	new_node.next = prev.next
	prev.next = new_node
	return dummy_head.head


def remove(head, index):
	if head is None:
		return None
	prev = search_by_index(index - 1)
	if prev is None:
		return
	elif prev.next is None:
		return
	else:
		pos.next = pos.next.next
		
		

def remove_vowel(head):
	'''
	dummy -> l -> m -> a -> o -> q -> r
		p    c
			 p    c
				  p    c 
				  p         c
				  p              c
								 p    c
	'''
	dummy_head = ListNode(head)
	dummy_head.next = head
	prev = dummy_head
	curr = head
	while curr is not None:
		if curr.val in ('a', 'e', 'i', 'o', 'u'):
			prev.next = curr.next
			curr = curr.next
		else:
			prev = prev.next
			curr = curr.next