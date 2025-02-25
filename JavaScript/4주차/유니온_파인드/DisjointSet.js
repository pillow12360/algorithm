class DisjointSet {
  constructor(size) {
    this.size = size;
    this.parents = Array.from({ length: size }, (_, i) => i); // 모든 노드의 부모를 자기 자신으로 설정
    this.rank = Array(size).fill(1); // 랭크(트리 높이)를 1로 초기화
  }

  // ✅ make(): 모든 원소의 부모를 자기 자신으로 초기화
  make() {
    this.parents = Array.from({ length: this.size }, (_, i) => i);
    this.rank = Array(this.size).fill(1);
  }

  // ✅ find(): 특정 원소의 대표(루트)를 찾음 (경로 압축 최적화)
  find(v) {
    if (this.parents[v] !== v) {
      this.parents[v] = this.find(this.parents[v]); // 경로 압축
    }
    return this.parents[v];
  }

  // ✅ union(): 두 집합을 합침 (랭크 기반)
  union(a, b) {
    let rootA = this.find(a);
    let rootB = this.find(b);

    if (rootA === rootB) return false; // 이미 같은 집합이면 합치지 않음

    // 랭크(트리 높이)가 높은 쪽이 부모가 됨
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

// ✅ 테스트 실행
const N = 6;
const ds = new DisjointSet(N);
ds.make();

ds.union(1, 2);
console.log(ds.parents); // [0, 1, 1, 3, 4, 5]

ds.union(3, 4);
console.log(ds.parents); // [0, 1, 1, 3, 3, 5]

ds.union(5, 3);
console.log(ds.parents); // [0, 1, 1, 3, 3, 3]

ds.union(1, 5);
console.log(ds.parents); // [0, 1, 1, 1, 3, 3]

console.log(ds.find(1)); // 1 (경로 압축됨)
console.log(ds.parents);

console.log(ds.find(4)); // 1 (경로 압축됨)
console.log(ds.parents);
