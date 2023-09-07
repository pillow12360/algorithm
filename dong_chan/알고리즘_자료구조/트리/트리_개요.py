# 9월4일

# binary Tree의 Node 구현

# class Node:
#   def __init__(self, value =0 , left = None, right = None):
#     self.value = value
#     self.left = left
#     self.right = right

# class BinaryTree:
#   def __init__(self):
#     self.root = None

# bt = BinaryTree()
# bt.root = Node(value=1)
# bt.root.left = Node(value=2)
# bt.root.right = Node(value=3)
# bt.root.left.left = Node(value=4)
# bt.root.left.right = Node(value=5)
# bt.root.right.right = Node(value=6)
# bt.root.right.left = Node(value=7)


from collections import deque


class Node():
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class BinaryTree():
    def __init__(self):
        self.root = None


bt = BinaryTree()
bt.root = Node(value=1)

# BFS 너비 우선 탐색 구현

# 방문과 접근은 다르다 방문은 그 노드에 접근해서 어떤 실행을 시키는 것
# 접근은 여러번 가능하다
# 방문은 방명록을 남기듯이 무엇인가 실행 해야 함 (visited 리스트에 append)
# visited 리스트는 마치 방명록 이다.


# 이 dfs 함수는 바로 코드를 작성 할 때 까지 충분히 숙지 해야함


# def bfs(root):
#     visited = []
#     # 방문한 노드를 append 한다

#     if root is None:  # 트리가 없다면 빈 리스트를 반환
#         return 0

#     q = deque()  # 큐를 사용해야한다. 복습 필요

#     q.append(root)
#     while q:
#         cur_node = q.popleft()
#         visited.append(cur_node.value)

#         if cur_node.left:
#             q.append(cur_node.left)
#         if cur_node.right:
#             q.append(cur_node.right)
#     return visited

# DFS
# 스택을 이용한 반복문 -> 생략
# 재귀를 이용한 반복문 by recursion

# 접근과 방문은 다름 방문은 딱 한번만

# 접근 하는 방법


# DFS 접근 순서

# 전위 순회

def preorder(cur_node):
    if cur_node is None:
        return
    print(cur_node.value)
    preorder(cur_node.left)
    preorder(cur_node.right)

# 자식 노드에 접근하기 전에 접근을 한다 -> 전위 순회


# 중위 순회 inorder

def inorder(cur_node):
    if cur_node is None:
        return
    inorder(cur_node.left)  # 접근했지만 방문을 하지 않고 left로 접근
    print(cur_node.value)
    print(cur_node.right)

# 후위순회 postorder 자식노드들의 방문이 완료되면 본인의 value를 접근


def postorder(cur_node):
    if cur_node is None:
        return
    postorder(cur_node.left)
    postorder(cur_node.right)
    postorder(cur_node.value)
