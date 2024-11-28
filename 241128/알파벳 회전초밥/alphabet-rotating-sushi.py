from collections import deque

A = input().strip()
word = deque(input().strip())

cnt = 1
curr_pos = 0  

while word:
    if curr_pos >= len(A):  
        curr_pos = 0 
        cnt += 1 
        
    if A[curr_pos] == word[0]: 
        word.popleft()
    
    curr_pos += 1

print(cnt)