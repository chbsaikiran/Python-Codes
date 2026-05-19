from collections import deque

def level_order(root):

    q = deque([root])

    while q:

        size = len(q)

        for _ in range(size):

            node = q.popleft()

            print(node.val)

            if node.left:
                q.append(node.left)

            if node.right:
                q.append(node.right)
