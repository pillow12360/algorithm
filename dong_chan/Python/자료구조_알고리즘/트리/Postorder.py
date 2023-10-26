# 09월 06일 인프런 강의 33강

# Tree 활용
# 1. Tree 구현 2. 트리 순회

# Lowest Common Ancestor of a Binary Tree
# 문제에서 Binary 트리 하나와 해당 트리에 속한 두 개의 노드가 주어진다. 이 대, 두 노드의 공통 조상중 가장 낮은 node 즉, the lowest common ancestor (LCA)를 찾아라


# 직관적으로 보았을 때, 서로의 조상을 타고 올라가다 보면 만나는 지점을 찾으면 된다.

# 각 노드의 조상 끼리 빔을 쏴본다. 한쪽에서만 빔이 들어오면, 통과 시키고, 빔 두개가 서로 만났을 때를 찾는다

# 케이스를 생각해보자

# 1번 빔이 아무것도 안들어 올 때 -> 어떤 빔도 쏠 수 없다.
# 2번 나 자신이 p 또는 q 일 때 (q와 p는 인풋 노드이다. ) -> 내 자신이 빔을 쏜다.  나 자신을 return 해준다.
# 3번 왼쪽 오른쪽 빔이 모두 들어오는 경우 l and r 내가 문제에서 원하던 공통 조상이다. 본인의 빔을 다시 쏜다 => 자신 return
# 4번 왼쪽 또는 오른쪽 한 곳에서만 빔이 들어온다. -> 새로운 빔을 만들지 않고 빔을 위쪽으로 흘려보내 준다. x(안들어오고) and l or r (에서 들어온다) l or r return

# 이 풀이는 직관을 이용한 풀이, 다른 풀이도 존재함


# 코드 설계
# Tree 문제인 것이 주어졌으니, Tree의 특성인 "재귀"를 이용한다.
# 재귀의 특성을 이용하여 생각할 경우가 작은 케이스를 바탕으로 코드를 설계해도 된다.
from collections import deque


class Node():
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class BianryTree():
    def __init__(self):
        self.root = None


Tr = BianryTree()
Tr.root = Node(value=1)


def LCA(root, p, q):
    if root == None:
        return None
    left = LCA(root.left, p, q)
    right = LCA(root.right, p, q)
    if root == p or root == q:  # q 또는 p 일경우
        return root
    elif left and right:  # 두 빔을 쏜경우
        return root
    # 이 코드 한 줄로 여러 케이스를 커버한다. 한쪽만 반환 되었을 때 그 반환값을 리턴함 (한쪽만 빔을 손경우)
    return left or right
# postorder와 원리가 비슷하다
# left와 right를 방문한 다음에 할 일을 하기 때문


def LCA(root, p, q):
    if root is None:
        return None

    left = LCA(root.left, p, q)
    right = LCA(root.right, p, q)

    if root == p or root == q:
        return root
    elif left and right:
        return root
    return left or right
