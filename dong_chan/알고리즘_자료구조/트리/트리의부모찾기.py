# 9월 6일 백준 문제 트리의 부모 찾기 실버2

import sys


class Node():
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# 내가 배웠던 트리와 약간 다른 듯 하다
# 내가 모르는 부분
# 입력 값을 트리 자료구조로 입력 하는 방법
# 문제가 정확히 어떤 뜻인지 파악 하는 것


# 입력값
'''
7
1 6
6 3
3 5
4 1
2 4
4 7
'''
# 출력값
'''
4
6
1
3
1
4
'''
# 트리의 루트를 1이라고 하였을 때 각 노드의 부모를 출력하는 프로그램


# 인터넷 답안 1


# 자기 호출 개수 제한
sys.setrecursionlimit(10**6)

# 테스트용 파일("input.txt") 읽기
# sys.stdin = open("input.txt", "r")

# 주어진 파일을 한 줄씩 입력
# input = sys.stdin.readline

# N 입력
N = int(input())

# tree, parent 초기화
tree = [[] for _ in range(N + 1)]  # 트리를 2 중 리스트로 초기화
parent = [None for _ in range(N + 1)]  # 부모를 저장할 빈 리스트를 초기화

# DFS 정의


def DFS(graph, vertex, visited):
    for i in graph[vertex]:
        # 만약 방문하지 않았을 경우 방문할 정점의 값을 할당하고 재귀함수 호출
        if not visited[i]:
            visited[i] = vertex
            DFS(graph, i, visited)


# 주어진 노드로 트리 값 할당
for _ in range(N - 1):
    node_a, node_b = map(int, input().split())
    tree[node_a].append(node_b)
    tree[node_b].append(node_a)

# DFS 함수 사용하여 parent 값 할당
DFS(tree, 1, parent)

# 각 노드의 부모 노드 번호를 2번부터 순서대로 출력
for i in range(2, N + 1):
    print(parent[i])
