let fs = require('fs');
let input = fs.readFileSync('io.txt').toString().split('\n').map(Number);

class Node {
  constructor(value) {
    this.value = value;
    this.left = null;
    this.right = null;
  }
}

class BST {
  constructor(value) {
    this.root = null;
    this.cnt = 0;
  }

  // insert(value) {
  //   this.cnt = 0;
  //   this._insert(value);
  //   console.log(cnt);
  // }

  insert(x) {
    if (this.root === null) {
      this.root = new Node(x);
      console.log(0);
    } else {
      this._insert(x, this.root);
    }
  }

  _insert(x, n) {
    this.cnt += 1;

    if (x < n.value) {
      if (n.left === null) {
        console.log(this.cnt);
        n.left = new Node(x);
      } else {
        this._insert(x, n.left);
      }
    } else if (x > n.value) {
      if (n.right === null) {
        console.log(this.cnt);
        n.right = new Node(x);
      } else {
        this._insert(x, n.right);
      }
    }
  }
}

let n = input.shift();
let arr = input;

// console.log(n, arr);

let bst = new BST();

for (let i of arr) {
  bst.insert(i);
}
