class MaxHeap {
  constructor() {
    this.heap = [];
  }

  getParentIndex(index) {
    return Math.floor((index - 1) / 2);
  }

  getLeftChildIndex(index) {
    return index * 2 + 1;
  }

  getRightChildIndex(index) {
    return index * 2 + 2;
  }

  push(v) {
    this.heap.push(v);
    this.heapifyUp();
  }

  /*
  1.	새 값을 배열 마지막에 삽입.
	2.	부모 노드와 비교:
	•	부모보다 크면 스왑(Swap)
	•	부모보다 작으면 종료
	3.	스왑 후 새로운 위치에서 다시 부모와 비교 (반복)
	4.	루트 노드에 도달하거나 부모보다 작으면 종료
  */

  heapifyUp() {
    let index = this.heap.length - 1;
    while (index > 0) {
      let parentIndex = this.getParentIndex(index);
      if (this.heap[index] <= this.heap[parentIndex]) break;
      [this.heap[index], this.heap[parentIndex]] = [
        this.heap[parentIndex],
        this.heap[index],
      ]; // swap
      index = parentIndex;
    }
  }

  /*
  heapifyDown() 흐름 요약
	1.	루트 노드 제거 후, 마지막 노드를 루트로 이동
	2.	왼쪽 & 오른쪽 자식 중 더 작은 값 찾기
	3.	부모가 자식보다 크다면 스왑
	4.	스왑한 위치에서 다시 자식과 비교 (반복)
	5.	힙 조건 만족 시 종료
  */

  heapifyDown() {
    let index = 0;
    const legth = this.heap.length;

    while (this.getLeftChildIndex(index) < length) {
      let leftChildIndex = this.getLeftChildIndex(index);
      let rightChildIndex = this.getRightChildIndex(index);
      let smallerChildIndex = leftChildIndex;

      if (
        rightChildIndex < length &&
        this.heap[rightChildIndex] < this.heap[leftChildIndex]
      ) {
        smallerChildIndex = rightChildIndex;
      }
    }
  }

  pop() {
    if (this.heap.length === 0) return null;
    if (this.heap.length === 1) return this.heap.pop();

    const minValue = this.heap[0];

    this.heap[0] = this.heap.pop();
    this.heapifyDown();
    return minValue;
  }

  size() {
    return this.heap.length;
  }
}
