# ! change LOCAL to False before submitting !
# set LOCAL to True for local testing

LOCAL = False

if LOCAL:

    class Node:
        def __init__(self, value, left=None, right=None):
            self.value = value
            self.right = right
            self.left = left


def solution(root, initial_root=None) -> bool:
    if initial_root is None:
        initial_root = root.value
    left_result = True
    right_result = True
    if root.left is not None:
        if root.left.value >= root.value:
            return False
        if initial_root >= root.left.value and initial_root < root.value:
            return False
        left_result = solution(root.left, initial_root) and solution(root.left)
    if root.right is not None:
        if root.value >= root.right.value:
            return False
        if root.right.value >= initial_root and initial_root > root.value:
            return False
        right_result = solution(root.right, initial_root) and solution(
            root.right
        )
    return left_result and right_result


def test():
    node1 = Node(1, None, None)
    node2 = Node(4, None, None)
    node3 = Node(3, node1, node2)
    node4 = Node(8, None, None)
    node5 = Node(5, node3, node4)

    assert solution(node5)
    node2.value = 5
    assert not solution(node5)


if __name__ == "__main__":
    test()
