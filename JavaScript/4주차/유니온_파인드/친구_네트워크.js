class DisjointSet {
  constructor(size) {
    this.size = Array(size).fill(1);
    this.parents = Array.from({ length: size }, (_, i) => i);
    this.rank = Array(size).fill(0);
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
    if (rootA === rootB) return this.size[rootA];
    // 두 집합을 합치고, 새로운 집합의 크기를 계산하는 로직 추가
    if (this.rank[rootA] < this.rank[rootB]) {
      this.parents[rootA] = rootB;
      this.size[rootB] += this.size[rootA];
      return this.size[rootB];
    } else {
      this.parents[rootB] = rootA;
      this.size[rootA] += this.size[rootB];
      if (this.rank[rootA] === this.rank[rootB]) this.rank[rootA]++;
      return this.size[rootA];
    }
  }
}

let fs = require('fs');
let input = fs.readFileSync('io.txt', 'utf-8').trim().split('\n');

let t = +input.shift();

while (t > 0) {
  let f = +input.shift();
  let arr = input.splice(0, f);

  // console.log(arr);

  let map = new Map();
  let dis = new DisjointSet(f * 2);
  let cur = 0;

  for (let i = 0; i < f; i++) {
    let [a, b] = arr[i].split(' ');
    if (!map.has(a)) {
      map.set(a, cur++);
    }
    if (!map.has(b)) {
      map.set(b, cur++);
    }

    const networkSize = dis.union(map.get(a), map.get(b));
    console.log(networkSize);
  }

  t--;
}
