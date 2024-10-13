# chat-gpt의 다시 풀어준 그리디 방식

S = list(input())
T = list(input())

while len(T) > len(S):
    if T[-1] == 'A':
        T.pop()
    elif T[-1] == 'B':
        T.pop()
        T.reverse()

print(1 if S == T else 0)
