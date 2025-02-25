class DisjointSet {
  constructor(size) {
    this.size = size;
    this.parents = Array.from({ length: size + 1 }, (_, i) => i);
    this.rank = Array(size + 1).fill(1); //  1-based index에 맞게 수정
  }

  find(v) {
    if (this.parents[v] !== v) {
      this.parents[v] = this.find(this.parents[v]); //  경로 압축 적용
    }
    return this.parents[v];
  }

  union(a, b) {
    let rootA = this.find(a);
    let rootB = this.find(b);

    if (rootA === rootB) return false; //  이미 같은 집합이면 합치지 않음

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
let input = fs.readFileSync('io.txt').toString().trim().split('\n');

let [n, m, k] = input.shift().split(' ').map(Number);
let pay = input.shift().split(' ').map(Number);

let dis = new DisjointSet(n);

// 친구 관계 연결
input = input.map((i) => i.split(' ').map(Number));
for (let i of input) {
  dis.union(i[0], i[1]);
}

//  부모 배열 출력 (경로 압축 적용 후)
// console.log(Array.from({ length: n }, (_, i) => dis.find(i + 1)));

//  각 그룹별 최소 친구비 찾기
let minCostGroup = new Map();

for (let i = 1; i <= n; i++) {
  let root = dis.find(i);
  if (!minCostGroup.has(root)) {
    minCostGroup.set(root, pay[i - 1]); //  친구비는 pay 배열에서 가져와야 함
  } else {
    minCostGroup.set(root, Math.min(minCostGroup.get(root), pay[i - 1]));
  }
}

// 최소 비용 계산
let minTotalCost = Array.from(minCostGroup.values()).reduce(
  (acc, cost) => acc + cost,
  0
);

//  친구를 모두 사귈 수 있는지 확인
console.log(minTotalCost <= k ? minTotalCost : 'Oh no');
