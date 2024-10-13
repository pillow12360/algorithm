# for 문과 if 문이 포함된 코드
N = int(input("최대 숫자를 입력 : "))

print(f"1부터 {N}까지 짝수 출력")
for i in range(1, N+1):
    if i % 2 == 0:
        print(i, end=" ")

print()

print(f"1부터 {N}까지 홀수 출력")
for i in range(1, N+1):
    if i % 2 != 0:
        print(i, end=" ")
