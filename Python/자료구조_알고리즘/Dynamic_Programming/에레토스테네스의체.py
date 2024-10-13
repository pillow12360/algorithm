def eratosthenes(N):
    set1 =set(range(2,N+1))
    for i in range(1,int(N**(1/2))+1):
        if i in set1:
            set1 -= set(range(2*i,N+1,i))
    return set1

N = 100
print(eratosthenes(N))

def sieve_of_eratosthenes(n):
    primes = set(range(2, n+1))
    
    for i in range(2, int(n**0.5) + 1): # 1부터 n의 제곱근까지 반복
        if i in primes: 
            primes -= set(range(2*i, n+1, i)) # i의 배수를 모두 차집합으로 제거
    
    return primes

print(sieve_of_eratosthenes(100))