from collections import deque


class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data



def insert(root, data):
    if root is None:
        return Node(data)

    if data < root.data:
        root.left = insert(root.left, data)
    else:
        root.right = insert(root.right, data)

    return root


def bfs(root):
    if root is None:
        return

    queue = deque()
    queue.append(root)

    while queue:
        node = queue.popleft()
        print(node.data, end=" ")

        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)

root = None
book_ids = [50, 30, 70, 20, 40, 60, 80]

for book in book_ids:
    root = insert(root, book)

print("Book IDs using BFS:")
bfs(root)