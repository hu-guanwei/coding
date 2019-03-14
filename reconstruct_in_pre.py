from binarytree import tree, Node

root = tree()
print(root)
inorder = [x.value for x in root.inorder]
preorder = [x.value for x in root.preorder]
postorder = [x.value for x in root.postorder]


def reconstruct(in_order, in_left, in_right,
                pre_order, pre_left, pre_right,
				in_dict):
	'''
	利用中序遍历和先序遍历重建二叉树
	'''
	assert(pre_right - pre_left == in_right - in_left)
	if in_left > in_right:
		return None
	
	root = Node(pre_order[pre_left])
	root_index = in_dict[root.value]
	left_size = root_index - in_left
	root.left = reconstruct(in_order, in_left, root_index - 1,
				pre_order, pre_left + 1, pre_left + left_size,
				in_dict)
	root.right = reconstruct(in_order, root_index + 1, in_right,
				pre_order, pre_left + left_size + 1, pre_right,
				in_dict)
				
	return root
	

in_dict = {j: i for i, j in enumerate(inorder)}

root = reconstruct(inorder, 0, len(inorder) - 1,
				   preorder, 0, len(preorder) - 1,
				   in_dict)

print(root)
	
