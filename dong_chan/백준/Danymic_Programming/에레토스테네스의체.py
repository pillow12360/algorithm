# def eratosthenes(N):
#     list1 =list(range(2,N+1))

#     route = N**(1/2)
    
    
    



# N = 100
# print(eratosthenes(N))




def sieve_of_eratosthenes(n):
    primes = set(range(2, n+1))
    
    for i in range(2, int(n**0.5) + 1):
        if i in primes:
            primes -= set(range(2*i, n+1, i))
    
    return primes

print(sieve_of_eratosthenes(100))