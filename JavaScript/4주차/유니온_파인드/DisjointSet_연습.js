class DisjointSet {
  constructor(size) {
    this.size = size;
    this.parents = Array.from({ length: size + 1 }, (_, i) => i);
    this.rank = Array(size + 1).fill(1);
  }

  find(v) {
    if (this.parents[v] !== v) {
      this.parents = find(this.parents[v]);
    }
    return this.parents[v];
  }

  union(a, b) {
    let rootA = find(a);
    let rootB = find(b);

    if (rootA === rootB) {
      return false;
    } else if (this.rank[rootA] > this.rank[rootB]) {
      this.parents[rootB] = rootA;
    } else if (this.rank[rootB] > this.rank[rootA]) {
      this.parents[rootA] = rootB;
    } else {
      this.parents[rootB] = rootA;
      this.rank[rootA]++;
    }
    return true;
  }
}
