# 9월 7일 인프런 강의 34강 levle order traversal 전반

# input, output 확인
# 코드 상에서 나올만한 오류를 예측 할 수 있다.

# input size N 확인

# 시간 복잡도를 계산하기 위한 input size N 또는 M 이 무엇인지 확인

# 제약조건 확인
# 시간복잡도 제한에 걸리지 않을지 -> 접근방법역시 생각 할 수 있다.

#  예상할 수 있는 오류 파악


# Maximum Depth of Binary Tree
# 문제에서 binary tree 하나가 주어진다. 주어진 binary tree의 최대 깊이를 반환하라
# 최대 깊이가 몇이냐?

# root노드와 얼마나 떨어져있나?

# root 노드만 있으면 깊이 1
# root 노드 외 아무 노드가 없으면 깊이 0

# 만약 1만개의 노드가 한 쪽으로만 있을 때, 내가 생각한 방식이 통할까? (극한 케이스)

# 제약 조건
# 0<= node개수 <= 10^4
# -100 <= Node.val <= 100 (Node.value값으로 활용할 것 이 없으니 크게 상관 x value 타입만 결정해줌)
# Node.value 값은 유니크 하지 않다 (중복 가능)

# 접근방법
# Tree 자료구조
# Tree 순회 - level order, post order


# 내가 한번 코드 구현을 해본다.
# level 순회 코드에서 변형만 해주면 된다.


from collections import deque


class Node():
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class BinaryTree():
    def __init__(self):
        self.root = None


# def MaxDepth(root):
#     max_depth = 0
#     if root is None:
#         return max_depth

#     q = deque()
#     q.append((root, 1))

#     while q:
#         cur_node, cur_depth = q.popleft()
#         max_depth = max(cur_depth, max_depth)
#         if cur_node.left:
#             q.append((cur_node.left, cur_depth+1))
#         if cur_node.right:
#             q.append((cur_node.right, cur_depth+1))

#     return max_depth


input = [3, 9, 20, None, None, 15, 7]  # 리스트를 트리 형태로 저장 해야함

root = Node(value=3)
root.left = Node(value=9)
root.right = Node(value=20)
root.right.left = Node(value=15)
root.right.right = Node(value=7)


def maxDepth(root):
    maxDepth = 0

    if root is None:
        return maxDepth

    q = deque()

    q.append((root, 1))

    while q:
        cur_node, cur_depth = q.popleft()
        maxDepth = max(maxDepth, cur_depth)
        if cur_node.left:
            q.append((cur_node.left, cur_depth+1))
        if cur_node.right:
            q.append((cur_node.right, cur_depth+1))

    return maxDepth


print(maxDepth(root))


# 0913 Step 2 postorder 후위순회

# level order 방식은 노드를 내려가면서 +1 씩하며 최대값 얻기

# 모든 노드에 방문을 하는데, 자손의 깊이를 비교하여 가장 깊은 레벨에 +1 

# postorder 모든 자식 노드를 방문 후 본인 방문 (방문 = 액션)


def postorder(root):
    if root is None:
        return 0
    
    leftDepth = postorder(root.left)
    rightDepth = postorder(root.right)

    return max(leftDepth,rightDepth) + 1 

print(postorder(root))
