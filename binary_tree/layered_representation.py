from structures.TreeNode import TreeNode


def get_layered_representation(root):
    result = []
    DFS(root, 0, result)
    return result


def DFS(node, depth, result):
    if not node:
        return

    if depth >= len(result):
        result.append([])

    result[depth].append(node.val)

    DFS(node.left, depth + 1, result)
    DFS(node.right, depth + 1, result)

n1 = TreeNode(2)
n2 = TreeNode(1)
n3 = TreeNode(3)

n1.left = n2
n1.right = n3

for layer in get_layered_representation(n1):
    print(layer)
