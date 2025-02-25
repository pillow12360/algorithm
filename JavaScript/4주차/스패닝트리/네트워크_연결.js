class DisjointSet {
  constructor(size) {
    this.size = size;
    this.parents = Array.from({ length: size + 1 }, (_, i) => i);
    this.rank = Array(size + 1).fill(1);
  }

  find(v) {
    if (this.parents[v] !== v) {
      this.parents[v] = this.find(this.parents[v]);
    }
    return this.parents[v];
  }

  union(a, b) {
    let rootA = this.find(a);
    let rootB = this.find(b);

    if (rootA === rootB) return false;
    if (this.rank[rootA] > this.rank[rootB]) {
      this.parents[rootB] = rootA;
    } else if (this.rank[rootA] < this.rank[rootB]) {
      this.parents[rootA] = rootB;
    } else {
      this.parents[rootB] = rootA;
      this.rank[rootA]++;
    }
    return true;
  }
}

let fs = require('fs');
let input = fs.readFileSync('io.txt').toString().split('\n');

let n = Number(input[0]);
let m = Number(input[1]);

let cost = input.slice(2).map((i) => i.split(' ').map(Number));

// console.log(n, m, cost);
cost.sort((a, b) => a[2] - b[2]); // 가중치 기준 오름차순 정렬

let ds = new DisjointSet(n);
let mstCost = 0;
let mstEdges = 0;

for (let [u, v, c] of cost) {
  if (ds.union(u, v)) {
    mstCost += c;
    mstEdges++;
    if (mstEdges === n - 1) break;
  }
}

console.log(mstCost);
