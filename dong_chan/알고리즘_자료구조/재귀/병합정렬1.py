# N, K = map(int, input().split())
# L = list(map(int, input().split()))


L = [4, 5, 1, 3, 2]


# def mergesort(L, p, r):
#     if p > r or p == r:
#         return L
#     if p < r:
#         q = (p+r)/2
#         mergesort(L, p, q)
#         mergesort(L, q+1, r)
#         merge(L, p, q, r)
#     return L


# def merge(L, p, q, r):
#     temp = []
#     i = p
#     j = q+1
#     t = 1
#     while (i <= q and j <= r):
#         if L[i] <= L[j]:
#             temp[t] = L[i]
#             t += 1
#             i += 1
#         else:
#             temp[t] = L[j]
#             t += 1
#             j += 1
#     while i <= q:
#         temp[t] = L[i]
#         t += 1
#         i += 1
#     while j <= r:
#         temp[t] = L[j]
#         t += 1
#         j += 1
#     i = p
#     t = 1
#     while i <= r:
#         L[i] = temp[t]
#         i += 1
#         t += 1
#     return L

# merge_sort(A[p..r]) { # A[p..r]을 오름차순 정렬한다.
#     if (p < r) then {
#         q <- ⌊(p + r) / 2⌋;       # q는 p, r의 중간 지점
#         merge_sort(A, p, q);      # 전반부 정렬
#         merge_sort(A, q + 1, r);  # 후반부 정렬
#         merge(A, p, q, r);        # 병합
#     }
# }

# # A[p..q]와 A[q+1..r]을 병합하여 A[p..r]을 오름차순 정렬된 상태로 만든다.
# # A[p..q]와 A[q+1..r]은 이미 오름차순으로 정렬되어 있다.
# merge(A[], p, q, r) {
#     i <- p; j <- q + 1; t <- 1;
#     while (i ≤ q and j ≤ r) {
#         if (A[i] ≤ A[j])
#         then tmp[t++] <- A[i++]; # tmp[t] <- A[i]; t++; i++;
#         else tmp[t++] <- A[j++]; # tmp[t] <- A[j]; t++; j++;
#     }
#     while (i ≤ q)  # 왼쪽 배열 부분이 남은 경우
#         tmp[t++] <- A[i++];
#     while (j ≤ r)  # 오른쪽 배열 부분이 남은 경우
#         tmp[t++] <- A[j++];
#     i <- p; t <- 1;
#     while (i ≤ r)  # 결과를 A[p..r]에 저장
#         A[i++] <- tmp[t++];
# }
