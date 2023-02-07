# Given the root to a binary tree, return the deepest node.


def increment_depth(node_depth_tuple):
    node, node_depth = node_depth_tuple
    return node, node_depth + 1


def deepest(node):
    if node and not node.left and not node.right:
        return node, 1
    if not node.left:
        return increment_depth(deepest(node.right))
    elif not node.right:
        return increment_depth(deepest(node.left))
    return max(deepest(node.left), deepest(node.right), key=lambda x: x[1])
