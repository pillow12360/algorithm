import sys

sys.setrecursionlimit(10**6)

def dfs(v):
  visited[v] = True

  for nv in graph[v]:
    if not visited[nv]:
      dfs(nv)
