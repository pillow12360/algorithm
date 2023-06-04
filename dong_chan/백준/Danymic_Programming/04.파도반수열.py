# 0604 파도반 수열 9461

'''
1,1,1,2,2,3,4,5,7,9
'''
# dp[4] = dp[1]+dp[2]
# dp[5] = dp[2]+dp[3]

# dp[i] = dp[i-3]+dp[i-2] 

# def fibonacci(n):
#     dp=[0]*(n+1)
#     dp[1],dp[2]=1,1
#     cnt2=0
#     for i in range(3,n+1):
#         cnt2+=1
#         dp[i]=dp[i-1]+dp[i-2]
#     return cnt2

#소요 시간 15분
#피보나치 수열을 참고하여 문제를 풀었음
def padoban(n):
    if n == 1 or n == 2 or n==3: #1번째부터 3번째는 식으로 구할 수 없으므로 직접 초기화
        return 1
    
    pd = [0]*(n+1) # 만들 파도반 요소 n+1개 리스트를 0으로 초기화
    pd[1],pd[2],pd[3] = 1,1,1 # 직접 초기화
    
    for i in range(4,n+1): #4번째부터는 동적 프로그래밍을 이용하여 구함
        pd[i] = pd[i-3]+pd[i-2]

    return pd[n]

m = int(input())

while m > 0:
    n = int(input())
    print(padoban(n))
    m -= 1