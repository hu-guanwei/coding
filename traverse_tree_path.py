from binarytree import tree

def preorder(root, path):
    if not root:
        return
    
    path.append(root.value)
    if root.left:
        preorder(root.left, path)
    else:
        path.append('#')

    if root.right:
        preorder(root.right, path)
    else:
        path.append('#')

def inorder(root, path):
    if not root:
        return []
    
    inorder(root.left, path)
    path.append(root.value)
    inorder(root.right, path)


def postorder(root, path):
    if not root:
        return []
    
    postorder(root.left, path)
    postorder(root.right, path)
    path.append(root.value)



root = tree()
print(root)

preorder_path = []
preorder(root, preorder_path)
print(preorder_path)

inorder_path = []
inorder(root, inorder_path)
print(inorder_path)

postorder_path = []
postorder(root, postorder_path)
print(postorder_path)

