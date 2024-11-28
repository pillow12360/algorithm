from collections import deque

A = list(input())

word = list(input())

word = deque(word)

cnt = 0

while word:
    cnt += 1
    a = word.popleft()

    for i in range(len(A)):
        if a == A[i] and word:
            a = word.popleft()

            continue



print(cnt)
    


    