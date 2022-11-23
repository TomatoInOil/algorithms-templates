# ! change LOCAL to False before submitting !
# set LOCAL to True for local testing

LOCAL = False

if LOCAL:

    class Node:
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.right = right
            self.left = left


def solution(root):
    result = True
    left_result = True
    right_result = True
    if root.left is not None:
        left_result = solution(root.left)
    if abs(get_height_of_tree(root.left) - get_height_of_tree(root.right)) > 1:
        result = False
    if root.right is not None:
        right_result = solution(root.right)
    return result and left_result and right_result


def get_height_of_tree(root):
    """Возвращает высоту дерева."""
    if root is None:
        return 0
    result = 1
    left_result = 0
    right_result = 0
    if root.left is not None:
        left_result += get_height_of_tree(root.left)
    if root.right is not None:
        right_result += get_height_of_tree(root.right)
    if right_result >= left_result:
        result += right_result
    else:
        result += left_result
    return result


def test():
    node1 = Node(1)
    node2 = Node(-5)
    node3 = Node(3, node1, node2)
    node4 = Node(10)
    node5 = Node(2, node3, node4)
    assert solution(node5)


if __name__ == "__main__":
    test()
