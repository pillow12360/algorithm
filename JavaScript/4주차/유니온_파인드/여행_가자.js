let fs = require('fs');
let input = fs.readFileSync('io.txt', 'utf-8').trim().split('\n');

let n = +input[0];
let m = +input[1];

let map = input.slice(2, 2 + n).map((i) => i.split(' ').map(Number));

class DisJointSet {
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
    } else if (this.rank[rootB] > this.rank[rootA]) {
      this.parents[rootA] = rootB;
    } else {
      this.parents[rootB] = rootA;
      this.rank[rootA]++;
    }
  }
}

let dis = new DisJointSet(n);

for (let i = 0; i < n; i++) {
  for (let j = 0; j < map[i].length; j++) {
    if (map[i][j] === 1) {
      dis.union(i + 1, j + 1);
    }
  }
}

let answer = input.slice(2 + n).map((i) => i.split(' ').map(Number))[0];

let jointSet = Array.from({ length: n + 1 }, (_, i) => dis.find(i));

// console.log(jointSet);

let temp = [];

for (let i of answer) {
  temp.push(jointSet[i]);
}

// console.log(temp);

let setAnswer = new Set(temp);

[...setAnswer].length === 1 ? console.log('YES') : console.log('NO');
