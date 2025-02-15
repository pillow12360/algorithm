let fs = require('fs');
let input = fs.readFileSync('io.txt').toString().split('\n');

let n = +input[0];
let arr1 = input[1].split(' ').map(Number);
let m = +input[2];
let arr2 = input[3].split(' ').map(Number);

arr1 = arr1.map((cur, index) => {
  return [cur, index];
});

let arr_map = new Map(arr1);

// console.log(arr_map);

arr2.forEach((a) => {
  if (arr_map.has(a)) {
    console.log(1);
  } else {
    console.log(0);
  }
});
