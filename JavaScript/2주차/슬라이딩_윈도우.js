// 고정 길이 슬라이딩 윈도우
// 크기가 3인 윈도우

let num = 3;

let arr = [1, 2, 3, 4, 13, 6, 7, 8, 9];

let window = 0;

for (let i = 0; i < num; i++) {
  window += arr[i];
}

let maxValue = window;

for (let i = num; i < arr.length; i++) {
  window += arr[i] - arr[i - num];
  maxValue = Math.max(window, maxValue);
}

console.log(maxValue);
