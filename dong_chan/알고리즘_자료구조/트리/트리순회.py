# 9월7일 백준 트리 순회 실버1

import sys


class Node():
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.left = right


class Tree():
    def __init__(self):
        self.root = None

# input 값을 트리에 저장할 함수 정의

# 루트 노드는 항상 A


def TreeInput(value, left, right):
    pass


# 정답 확인 = 딕셔너리를 이용한 트리

N = int(sys.stdin.readline().strip())
tree = {}

for n in range(N):
    root, left, right = sys.stdin.readline().strip().split()
    tree[root] = [left, right]


def preorder(root):
    if root != '.':
        print(root, end='')  # root
        preorder(tree[root][0])  # left
        preorder(tree[root][1])  # right


def inorder(root):
    if root != '.':
        inorder(tree[root][0])  # left
        print(root, end='')  # root
        inorder(tree[root][1])  # right


def postorder(root):
    if root != '.':
        postorder(tree[root][0])  # left
        postorder(tree[root][1])  # right
        print(root, end='')  # root


preorder('A')
print()
inorder('A')
print()
postorder('A')

# 문제 이해
# input 값의 타입은 무엇인가 ?
# n 의 범위
# output
