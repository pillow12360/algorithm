let fs = require('fs');
let input = fs.readFileSync('io.txt').toString().trim().split('\n');

let n = parseInt(input.shift());
let arr = input.map((a) => a.split(' '));

class Node {
  constructor(value) {
    this.value = value;
    this.left = null;
    this.right = null;
  }
}

class BT {
  constructor() {
    this.root = null;
    this.nodes = {}; // 노드 저장용 객체
  }

  insert(value, left, right) {
    if (!this.nodes[value]) this.nodes[value] = new Node(value);
    if (left !== '.') this.nodes[left] = new Node(left);
    if (right !== '.') this.nodes[right] = new Node(right);
    if (left !== '.') this.nodes[value].left = this.nodes[left];
    if (right !== '.') this.nodes[value].right = this.nodes[right];

    if (!this.root) this.root = this.nodes['A']; // 루트 설정
  }

  // 📌 전위 순회 (Preorder)
  preOrder() {
    this._preorderRec(this.root);
    console.log();
  }

  _preorderRec(node) {
    if (!node) return;
    process.stdout.write(node.value);
    this._preorderRec(node.left);
    this._preorderRec(node.right);
  }

  // 📌 중위 순회 (Inorder)
  inOrder() {
    this._inorderRec(this.root);
    console.log();
  }

  _inorderRec(node) {
    if (!node) return;
    this._inorderRec(node.left);
    process.stdout.write(node.value);
    this._inorderRec(node.right);
  }

  // 📌 후위 순회 (Postorder)
  postOrder() {
    this._postorderRec(this.root);
    console.log();
  }

  _postorderRec(node) {
    if (!node) return;
    this._postorderRec(node.left);
    this._postorderRec(node.right);
    process.stdout.write(node.value);
  }
}

let bt = new BT();

for (let i of arr) {
  // console.log(i);
  bt.insert(i[0], i[1], i[2]);
}

bt.preOrder();
bt.inOrder();
bt.postOrder();
