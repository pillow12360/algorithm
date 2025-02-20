let fs = require('fs');
let input = fs.readFileSync('io.txt').toString().trim().split('\n').map(Number);

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
    this.counter = 0;
  }

  insert(value) {
    // 루트가 없는 경우 (첫 번째 노드)
    if (this.root === null) {
      this.root = new Node(value);
      return this.counter; // 카운터 반환 (0)
    }

    return this._insertRec(this.root, value);
  }

  _insertRec(node, value) {
    this.counter++; // 비교 연산 카운터 증가

    if (value < node.value) {
      // 왼쪽 자식이 없으면 새 노드 생성
      if (node.left === null) {
        node.left = new Node(value);
        return this.counter;
      }
      // 왼쪽 자식이 있으면 재귀적으로 삽입
      return this._insertRec(node.left, value);
    } else {
      // 오른쪽 자식이 없으면 새 노드 생성
      if (node.right === null) {
        node.right = new Node(value);
        return this.counter;
      }
      // 오른쪽 자식이 있으면 재귀적으로 삽입
      return this._insertRec(node.right, value);
    }
  }
}

const n = input[0];
const bst = new BST();
const results = [];

// 첫 번째 수는 루트로 설정하고 C=0 출력
results.push(bst.insert(input[1]));

// 나머지 수를 순서대로 삽입
for (let i = 2; i <= n; i++) {
  results.push(bst.insert(input[i]));
}

console.log(results.join('\n'));
