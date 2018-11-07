class TreeNode(object):
    def __init__(self, val):
	self.val = val
	self.left = None
	self.right = None 
		


'''
      10                         10: in (-inf, +inf)
     /   \           5 in (-inf, 10)   12 in (10, +inf)
    5    12
   / \   / \
  3   7 11  13   
'''		
		
root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(12)
root.left.left = TreeNode(3)
root.left.right = TreeNode(7)
root.right.left = TreeNode(11)
root.right.right = TreeNode(13)
	
		

def is_bst(root):
    m = float('-inf')
    M = float('+inf')
	return __is_bst(root, m, M)

def __is_bst(root, low, high):
    if not root:
	return True
    if not low < root.val < high:
	return False
    return __is_bst(root.left, low, root.val) and __is_bst(root.right, root.val, high)
	
print(is_bst(root))
