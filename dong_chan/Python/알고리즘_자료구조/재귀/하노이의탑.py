# 하노이의 탑 자료구조 공부 10월14일

# 재귀

def hanoi(n,A,B,C):
  if n == 1:
    print(f"1번 타워를 {A}에서 {C}로 이동")
  else:
    hanoi(n-1,A,C,B)
    print(f"{n}번타워를 {A}에서 {C}로 이동")
    hanoi(n-1,B,A,C)

n = 4
print(hanoi(n,'A','B','C'))