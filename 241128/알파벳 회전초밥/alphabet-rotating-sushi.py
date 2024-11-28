from collections import deque

A = list(input())

word = list(input())

word_len = len(word)

word = deque(word)

cnt = 0


a = word.popleft()

for i in A:
    if a == i:
        cnt += 1
        if word:
            a = word.popleft()

answer = word_len - cnt + 1

print(answer)