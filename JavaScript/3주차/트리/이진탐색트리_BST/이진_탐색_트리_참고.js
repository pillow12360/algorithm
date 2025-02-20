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
  constructor() {
    this.root = null;
  }

  insert(x) {
    let count = 0;

    if (this.root === null) {
      this.root = new Node(x);
      console.log(count);
      return;
    }

    let current = this.root;

    while (true) {
      count += 1;
      if (x < current.value) {
        if (current.left === null) {
          current.left = new Node(x);
          console.log(count);
          return;
        }
        current = current.left;
      } else {
        if (current.right === null) {
          current.right = new Node(x);
          console.log(count);
          return;
        }
        current = current.right;
      }
    }
  }
}

let n = input.shift();
let bst = new BST();

for (let i of input) {
  bst.insert(i);
}
