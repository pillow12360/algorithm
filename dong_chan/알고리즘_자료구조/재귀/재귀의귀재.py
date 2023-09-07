

def recursion(S, l, r):
    global cnt
    cnt += 1

    if l >= r:
        return 1

    elif S[l] != S[r]:
        return 0
    else:
        return recursion(S, l+1, r-1)


def ispalindrome(S):
    return recursion(S, 0, len(S)-1)


N = int(input())

for i in range(N):
    M = input()
    cnt = 0
    print(ispalindrome(M), cnt)
