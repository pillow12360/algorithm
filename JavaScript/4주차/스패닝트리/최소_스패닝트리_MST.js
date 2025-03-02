class DisjointSet {
  constructor(size) {
    this.size = size;
    this.parents = Array.from({ length: size }, (_, i) => i);
    this.rank = Array(size).fill(0);
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
    else if (this.rank[rootA] > this.rank[rootB]) {
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

function MST(n, graph) {
  graph = graph.sort((a, b) => a[2] - b[2]);

  let dis = new DisjointSet(n);
  let mst = [];
  let weight = 0;

  for (let [u, v, w] of graph) {
    if (dis.union(u, v)) {
      mst.push([u, v, w]);
      weight += w;
      if (mst.length === n - 1) break;
    }
  }
  return weight;
}

let fs = require('fs');
let input = fs.readFileSync('io.txt', 'utf-8').trim().split('\n');

let [V, E] = input[0].split(' ');
let graph = input.slice(1).map((i) => {
  let [A, B, C] = i.split(' ').map(Number);
  return [A - 1, B - 1, C]; // 1-based index를 0-based index로 변환
});
// console.log(graph);

console.log(MST(V, graph));
