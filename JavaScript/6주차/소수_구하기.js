let fs = require('fs');
let [m, n] = fs.readFileSync('io.txt').toString().split(' ').map(Number);

console.log(m, n);

let arr = Array.from({ length: n + 1 }, (_, i) => i);

let primes = new Array(n + 1).fill(true);
primes[0] = primes[1] = false;

for (let i = 2; i * i <= n; i++) {
  if (primes[i]) {
    for (let j = i * i; j <= n; j += i) {
      primes[j] = false;
    } // i의 배수들을 제거
  }
}

primes
  .map((isPrime, index) => (isPrime ? index : null))
  .filter((val) => val !== null);

console.log(primes);
console.log(arr);

arr.map((i,))