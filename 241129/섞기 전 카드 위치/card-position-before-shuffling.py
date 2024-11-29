n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split())) #3번 반복한 이후의 카드 상태

a = [i-1 for i in a]

mix_b = []
# i는 index, j는 value
for _ in range(3):
    

    for i in a:
        mix_b.append(b[i])

    # print(mix_b)

    b = mix_b
    mix_b = []

    
for i in b:
    print(i)