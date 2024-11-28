from collections import deque

A = input().strip()
word = deque(input().strip())

cur_pos = 0
cnt = 1

while word:

    if cur_pos >= len(A):
        cur_pos = 0
        cnt += 1

    if A[cur_pos] == word[0]:
        word.popleft()

    cur_pos += 1
        
print(cnt)
    

    
