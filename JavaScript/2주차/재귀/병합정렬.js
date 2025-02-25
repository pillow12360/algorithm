function mergeSort(arr, depth = 0) {
  console.log(`${'  '.repeat(depth)}🚀 현재 배열:`, arr);

  if (arr.length <= 1) return arr; // 길이가 1 이하라면 이미 정렬된 상태

  const mid = Math.floor(arr.length / 2);

  const left = mergeSort(arr.slice(0, mid), depth + 1); // 왼쪽 절반 정렬

  const right = mergeSort(arr.slice(mid), depth + 1); // 오른쪽 절반 정렬

  const merged = merge(left, right);
  console.log(`${'  '.repeat(depth)}🔄 병합된 결과:`, merged);
  return merged;
}

function merge(left, right) {
  let sortedArray = [];
  let i = 0,
    j = 0;

  while (i < left.length && j < right.length) {
    if (left[i] < right[j]) {
      sortedArray.push(left[i++]);
    } else {
      sortedArray.push(right[j++]);
    }
  }

  return [...sortedArray, ...left.slice(i), ...right.slice(j)];
}

// 실행
const arr = [38, 27, 43, 3, 9, 82, 10];
console.log('📌 정렬 전:', arr);
const sortedArr = mergeSort(arr);
console.log('✅ 정렬 완료:', sortedArr);
