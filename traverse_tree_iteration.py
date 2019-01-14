from binarytree import tree, Node

def preorder(root):
    if not root:
        return []

    path = []
    stack = [(root, 1)]
    
    while stack:
        node, cnt = stack.pop()
        if cnt == 1:
            path.append(node.value)
            stack.append((node, cnt + 1))
            if node.left:
                stack.append((node.left, 1))
        elif cnt == 2:
            if node.right:
                stack.append((node.right, 1))
    
    return path

root = tree()
print(root)

preorder_path = preorder(root)
print(preorder_path)
