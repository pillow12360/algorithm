let fs = require('fs');
let input = fs.readFileSync('io.txt').toString().trim().split('\n');
let [n, m] = input[0].split(' ').map(Number);

let arr = input.slice(1).map((i) => i.split(' ').map(Number));
// console.log(n, m, arr);

class DisjointSet {
  constructor(size) {
    this.size = size;
    this.parents = Array.from({ length: size + 1 }, (_, i) => i);
    this.rank = Array(size + 1).fill(1);
  }

  find(v) {
    if (v !== this.parents[v]) {
      this.parents[v] = this.find(this.parents[v]);
    }
    return this.parents[v];
  }

  union(a, b) {
    let rootA = this.find(a);
    let rootB = this.find(b);

    if (rootA === rootB) return false;
    else if (this.rank[rootA] > this.rank[rootB]) {
      this.parents[rootB] = rootA;
    } else if (this.rank[rootA] < this.rank[rootB]) {
      this.parents[rootA] = rootB;
    } else {
      this.parents[rootB] = rootA;
      this.rank[rootA] += 1; // 같은 높이면 한쪽의 높이를 증가
    }

    return true;
  }
}

let dis = new DisjointSet(n);

for (let [com, a, b] of arr) {
  if (com === 0) {
    dis.union(a, b);
    continue;
  }
  dis.find(a) === dis.find(b) ? console.log('YES') : console.log('NO');
}

/*
백준에서 Node.js를 이용하여 문제를 푸실 때, 일부 문제에 한하여 fs 모듈을 사용하여 문제를 푸실 경우, 코드가 잘못된 것 같지 않은데도 런타임 에러(EACCES)를 받으신 적이 있으실 겁니다. 이로 인해 다른 언어로 문제를 풀거나, readline 모듈을 사용하는 코드로 다시 수정해서 제출하셨을 거에요.

Node.js의 fs 모듈을 사용할 경우 런타임 에러(EACCES)가 발생하는 문제를 몇 가지 나열해 보자면 아래와 같습니다.

14681
11536
11508
런타임 에러(EACCES)는 권한이 없어서 생기는 에러이며, 여러분의 코드에서 입력을 불러올 때 경로가 "/dev/stdin" 인 경우 상기의 문제를 포함한 일부분의 문제에서 발생할 수 있습니다.

이 경우, readFileSync(0, "utf-8") 과 같이 경로를 변경해 주시면 런타임 에러(EACCES)가 발생하지 않게 될 것입니다. 문제를 푸시는 데 참고하시기 바라며, 앞으로도 입력을 받아오실 때에는 이 경로를 적극 사용해 주실 것을 권장드립니다.

아래는 1000번 문제를 변경한 경로를 사용하여 문제를 푸는 코드의 예시입니다.

1
const fs = require('fs');
2
const [A, B] = fs.readFileSync(0, 'utf-8').trim().split(' ').map(Number);
3
​
4
console.log(A + B);
5
​
*/
