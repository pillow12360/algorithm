# N, K = map(int, input().split())
# L = list(map(int, input().split()))


L = [4, 5, 1, 3, 2]


def mergesort(L, p, r):
    if p > r or p == r:
        return L
    if p < r:
        q = (p+r)/2
        mergesort(L, p, q)
        mergesort(L, q+1, r)
        merge(L, p, q, r)
    return L


def merge(L, p, q, r):
    temp = []
    i = p
    j = q+1
    t = 1
    while (i <= q and j <= r):
        if L[i] <= L[j]:
            temp[t] = L[i]
            t += 1
            i += 1
        else:
            temp[t] = L[j]
            t += 1
            j += 1
    while i <= q:
        temp[t] = L[i]
        t += 1
        i += 1
    while j <= r:
        temp[t] = L[j]
        t += 1
        j += 1
    i = p
    t = 1
    while i <= r:
        L[i] = temp[t]
        i += 1
        t += 1
    return L


print(mergesort(L, 0, 4))
