#1월1일 그리디 골드 5
# A와 B



# 수정 전 

S = list(input())
T = list(input())

# print(S,T)

# Top - down 방식 풀이
dap = False

while T:

  if T[-1] == 'A':
    T.pop()

  elif T[-1] == 'B':
    T.pop()

    T.reverse() # 이부분을 단순히 for 문으로 서로 바꾸어주는 로직이 반례가 생겨 해맸다.

  if T == S:
    dap = True
    break

if dap:
  print(1)
else:
  print(0)


# 수정 후
  
  # 수정
S = list(input())
T = list(input())

# print(S,T)

# Top - down 방식 풀이
dap = False

while T:

  if T[-1] == 'A':
    T.pop()

  elif T[-1] == 'B':
    T.pop()
    T.reverse()

  if S == T:
    dap = True
    break
  

if dap:
  print(1)
else:
  print(0)


# 알게된 점
  
# 반례 꼼꼼 히 확인 for 문 인덱스에서 문제 생김
# reverse() 함수를 활용하여 A, B를 바꾸어주는 로직

# 슬라이싱을 활용해서 리스트 뒤집기
# my_list = [1, 2, 3, 4, 5]
# reversed_list = my_list[::-1]
# print(reversed_list)  # 출력: [5, 4, 3, 2, 1]