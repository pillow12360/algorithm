#24416 피보나치 수 1 0531

n = int(input())

class fiboClass():
    def init(self):
        self.cnt = 0

    def fib(self,n):
        cnt = cnt + 1
        if n == 1 or n ==2:
            return 1
        else:
            return self.fib(n-1)+self.fib(n-2)

    def fibonacci(self,n):
        self.cnt = self.cnt + 1
        f = [1, 1]  
        
        for i in range(2, n):
            f.append(f[i-1] + f[i-2]) 
        
        return f[n-1]

fibo = fiboClass()

fibo.fib(n)
fibo.fibonacci(n)

print(fibo.cnt)
