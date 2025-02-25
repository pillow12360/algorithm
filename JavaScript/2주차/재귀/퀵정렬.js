function quickSort(arr) {
  if (arr.length <= 1) return arr; // 요소가 하나면 이미 정렬됨

  const pivot = arr[Math.floor(arr.length / 2)]; // 피벗 선택 (가운데 값)
  const left = arr.filter((num) => num < pivot); // 피벗보다 작은 값
  const middle = arr.filter((num) => num === pivot); // 피벗과 같은 값
  const right = arr.filter((num) => num > pivot); // 피벗보다 큰 값
  console.log(`pivot`, pivot);
  console.log(`left`, left);
  console.log(`right`, right);
  console.log(`middle`, middle);

  return [...quickSort(left), ...middle, ...quickSort(right)];
}

console.log(quickSort([5, 3, 8, 4, 2, 7, 1, 10]));
