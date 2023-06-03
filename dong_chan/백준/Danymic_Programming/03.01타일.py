import math
# 6월3일 
# 만들 자리 수

# 동적 계획법 : 일부의 작은 결과값을 반복하여 결론 도출
'''먼저 
1. A로 만들 수 있는 모든 순열
2. B로 만들 수 있는 모든 순열 
3. A와 B 합쳐서 만들 수 있는 모든 순열

1,2,3의 자릿수를 모두 더하는 것

'''

'''
00을 최대한 많이 사용하는 조합을 구하고 차례대로 가장 적게 사용 하는 경우의 수까지 반복하는 것

n = 4
0000 0011 1100 1001 1111
n=5
00001 00100 10000
00111 11001 00111
11111
n = 6
000000 
000011 001100 110000
001111 100111 110011 11100
111111


00을 다른 문자 하나로 치환 1도 x로 치환
n = 6
Z = 00
z,z,z 의 순열 
z,z,1,1 의 순열
z,1,1,1,1 의 순열
의 수를 모두 더해서 풀기
'''
'''
N = 6

cnt = 6//2
answer = []
list1 = []

for i in range(0,cnt+1): #1부터 사용할 z의 
    list1=[]
    cnt1 = 0
    if not i==0:
        for j in range(1,i+1):
            list1.append("Z")
            cnt1 += 1
    
    while len(list1)-cnt1 < N-(i*2): #자리수가 N이 될때 까지 x를 채워넣어줌
        list1.append("X")
    print(list1)
    permu = itertools.combinations(list1,i)
    answer.append(list(permu))

print(answer)

'''
N = int(input())

cnt = N//2
answer = 0

for i in range(0,cnt+1): #1부터 사용할 z의 
    list1=[]
    cnt1 = 0
    if not i==0:
        for j in range(1,i+1):
            list1.append("Z")
            cnt1 += 1
    
    while len(list1)-cnt1 < N-(i*2): #자리수가 N이 될때 까지 x를 채워넣어줌
        list1.append("X")
    permu = math.comb(len(list1),len(list1)-cnt1)
    answer+=permu

print(answer)

#시간 초과 에러




