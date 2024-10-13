# 11월 06일 브루트 포스 실버 4
# 체스판 다시 칠하기

N, M = map(int,input().split())

chess = []

for i in range(N):
  chess.append(input())
# 입력값 처리

# 생각해야 할 것

# 8 x 8 체스판을 구해야 함
# 색칠해야 하는 것이 가장 적은 체스판을 구해야 하지만, 특별하게 새보지 않고 구할 방법이 없다.
# 그러니 8 x 8 체스의 모든 칸을 2중 for 문으로 순회하는 도중
# 2중 for문을 이용하여 색칠해야 하는 수를 모두 구한 후
# 가장 색칠해야 하는 가지 수 가 적은 경우를 출력한다.
# 가장 적은 체스판을 바꾸어야 하는 체스판 리턴

result = [] # 색칠하는 칸의 개수를 구한 값을 저장할 리스트

# 모든 체스판을 순회하며 색칠 해야 할 값 구한다.

for i in range(N-7): # 8 x 8 체스판이 만들어 질 수 있는 시작점의 범위
  for j in range(M-7): 

    drawB = 0 # 검은색을 색칠 해야 해야하는 수
    drawW = 0

    for a in range(i, i+8): # 여기서 부터 정답 참조
      for b in range(j, j+8): # 8x8의 체스판을 만들어야 함으로

        if (a+b) % 2 == 0: # 체스판의 왼쪽 맨위가 W 일 경우

          if chess[a][b] != "B":
            drawB += 1
          if chess[a][b] != "W":
            drawW += 1

        else: # 체스판의 왼쪽 맨위가 B일 경우

          if chess[a][b] != "W":
            drawB += 1
          if chess[a][b] != "B":
            drawW += 1

    result.append(drawB) # 검은색으로 칠하는 수
    result.append(drawW) # 흰색으로 칠하는 수

print( min(result) )