from binarytree import tree, Node

root = tree()
print(root)
in_order = [x.value for x in root.inorder]
pre_order = [x.value for x in root.preorder]
post_order = [x.value for x in root.postorder]


def reconstruct(in_order, in_left, in_right,
                post_order, post_left, post_right,
                in_dict):
    '''
    利用中序遍历和后序遍历重建二叉树
    '''
    assert(in_right - in_left == post_right - post_left)
    if in_left > in_right:
        return
        
        
    root = Node(post_order[post_right])
    root_index = in_dict[root.value]
    left_size = root_index - in_left
    
    root.left = reconstruct(in_order, in_left, root_index - 1,
                            post_order, post_left, post_left + left_size - 1,
                            in_dict)
    root.right = reconstruct(in_order, root_index + 1, in_right,
                             post_order, post_left + left_size, post_right - 1,
                             in_dict)
    
    
    return root
    

in_dict = {j: i for i, j in enumerate(in_order)}
root = reconstruct(in_order, 0, len(in_order) - 1,
                   post_order, 0, len(post_order) - 1,
                   in_dict)
print(root)
                   