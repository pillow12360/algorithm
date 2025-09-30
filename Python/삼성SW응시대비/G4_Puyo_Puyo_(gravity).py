from collections import deque

grid = [list(input()) for _ in range(12)]

answer = 0

def is_range(r,c):
  return 0<=r<12 and 0<=c<6

# 발상의 전환 한 row만 선택하여 중력을 적용 
# 중요!!
def gravity():
  for c in range(6):
    q = deque()
    for r in range(11,-1,-1):
      if grid[r][c] != '.':
        q.append(grid[r][c])

    for r in range(11,-1,-1):
        grid[r][c] = '.'

    for r in range(11,-1,-1):
      if q:
        grid[r][c] = q.popleft()

drc = [(-1,0),(1,0),(0,-1),(0,1)] # 상하좌우

'''
BFS

R은 빨강, G는 초록, B는 파랑, P는 보라, Y는 노랑
'''

def bfs(r,c,color):
  visited = [[False] * 6 for _ in range(12)]
  q = deque()
  cnt = 0
  del_q = [[r,c]]
  q.append([r,c])

  while q:
    cr, cc = q.popleft()

    for i in range(4):
      nr = cr + drc[i][0]
      nc = cc + drc[i][1]

      if is_range(nr,nc) and not visited[nr][nc]:
        if grid[nr][nc] == color:
          visited[nr][nc] = True
          q.append([nr,nc])
          del_q.append([nr,nc])
          cnt += 1

  if cnt > 3:
    for i, j in del_q:
      grid[i][j] = '.'
    return True

  return False

'''
while

뿌요가 상하좌우 같은 색이 인접함 여부를 판별
else: break
판별한 뿌요를 삭제, 여러 그룹이여도 하나의 연쇄
중력 적용
answer +1
'''

colors = ['R','G','B','P','Y']

while True:
  is_pung = False

  for color in colors:
    for i in range(12):
      for j in range(6):
        if grid[i][j] == color and bfs(i,j,color):
          is_pung = True
  
  if is_pung == False:
    break
  else:
    answer += 1

  gravity()

print(answer)
