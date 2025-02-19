class Node {
  constructor(value) {
    this.value = value;
    this.right = null;
    this.left = null;
  }
}

class BST {
  constructor() {
    this.root = null;
  }

  insert(value) {
    this.root = this._insertRec(this.root, value);
  }

  _insertRec(node, value) {
    if (!node) return new Node(value); // 처음 값을 넣는 경우
    if (value < node.value) node.left = this._insertRec(node.left, value);
    // 현재 노드보다 넣는 값이 작은경우 (재귀)
    else node.right = this._insertRec(node.right, value); // 반대로 클 경우 오른쪽 노드에 추가 (재귀)
    return node; // 모두 수행하면 return
  }

  search(value) {
    return this._searchRec(this.root, value);
  }

  _searchRec(node, value) {
    if (!node) return false;
    if (node.value === false) return true;
    return value < node.value
      ? this._searchRec(node.left, value)
      : this._searchRec(node.right, value); // 재귀
  }

  inorder() {
    this._inorderRec(this.root);
    console.log();
  }
  _inorderRec(node) {
    if (!node) return;
    this._inorderRec(node.left);
    process.stdout.write(node.value + ' ');
    this._inorderRec(node.right);
  }
}

let bst = new BST();

bst.insert(10);
bst.insert(20);
bst.insert(30);
bst.insert(1);
bst.insert(2);
bst.insert(3);
bst.insert(4);
bst.insert(5);

console.log('탐색 7:', bst.search(7)); // true
console.log('탐색 8:', bst.search(8)); // false
bst.inorder();

/*

BFS
가중치가 없는 map에서 s->e 최소 비용(거리)를 구할때 O(n)
특정위치에서 점진적으로 퍼져나가는 

DFS
start -> end로 가는 모든 방법의 수 구할 때

다익스트라 O(n^2)
가중치가 있는 map에서 start -> end 까지 최소 거리를 구할때

프로이드워셜 DP
- 모든 노드들의 최소 비용을 모두 구함 O(n^3)

완전 탐색

- search
  Squencial Search

- 경우의 수 
순열, 조합, 집합

- 그래프, 트리
  DFS, BFS
  
Search + 분할정복 -> 이진 탐색
슬라이딩 윈도우 
투 포인터

*/
