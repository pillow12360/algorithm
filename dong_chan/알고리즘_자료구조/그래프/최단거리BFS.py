# 0916 인프런강의 최단거리 BFS

# Shortest Path in Binary Matrix

# n * n binary matrix 인 gird가 주어졌을 때, 출발지에서 목적지 까지 도착하는 가장 빠른 경로의 길이를 반환하시오. 만약 경로가 없다면 -1 반환

# 정사각형 grid n x n
# 1<=n<=100

# 갈 수 없는 1은 연결되어있지 않다고 가정하면 그래프 형태로 생각을 확장 할 수 있다.

# Bfs 의 특성상 가까운 벌텍스 부터 방문하기 때문에 마치 파동이 퍼져나가듯 방문을 하게 된다. 

# 방문할 때마다 벌텍스에 거리를 저장

# dfs로도 풀 수 있지만, 효율적이지 않다. 최단거리, 미로 문제는 bfs로 푼다.


# 최단 거리 bfs

grid = [
  [0,0,0,1,0,0,0],
  [0,1,1,1,0,1,0],
  [0,1,0,0,0,1,0],
  [0,0,0,1,1,1,0],
  [0,1,0,0,0,0,0]
]

from collections import deque

def shortestPathBinaryMatrix(gird):
  shortest_path_len = -1 # -1로 초기화 도착할 수 없을 때

  row = len(gird)
  col = len(gird[0])

  if grid[0][0] != 0 or grid[row-1][col-1] != 0:
    return shortest_path_len

  queue = deque() # 튜플은 여기다 바로 쓸 수 없다
  queue.append((0,0,1))

  visited = [[False]*col for _ in range(row)] # 방문했음을 표시하는 그리드(리스트) , 방문할 때 마다 True로 표시

  visited[0][0] = True
  
  delta = [(1,0), (-1,0), (0,1), (0,-1), (1,1), (1,-1), (-1,1), (-1,-1)]

  while queue:
    cur_r, cur_c, cur_len = queue.popleft() 

    # 목적지에 도착했을 때 그 때 cur_len를 shortest_path_len에 저장하면 된다.

    if cur_r == row - 1 and cur_c == col - 1:
      shortest_path_len = cur_len
      break

    for dr, dc in delta:
      next_r = cur_r + dr
      next_c = cur_c + dc

      if next_r >= 0 and next_r < row and next_c >= 0 and next_c < col:
        if gird[next_r][next_c] == 0 and not visited[next_r][next_c]:
          queue.append((next_r,next_c,cur_len+1))
          visited[next_r][next_c] = True

  return shortest_path_len

print(shortestPathBinaryMatrix(grid))

