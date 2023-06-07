#다양한 수로 이루어진 배열이 있을 때 주어진 수들을 M번 더하여 가장 큰 수를 만드는 법칙.

#단 배열의 특정한 인덱스에 해당하는 수가 연속해서 K번을 초과하여 더해질 수 없다

N, M, K = map(int,(input().split()))

N = list(map(int,input().split()))


N = sorted(N,reverse=True)

print(N)


