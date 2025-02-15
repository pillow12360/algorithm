let fs = require('fs');
let input = fs.readFileSync('io.txt').toString().split('\n');

let n = +input[0];
let arr = input[1].split(' ').map(Number);

let person = [];
for (let i = arr.length - 1; i >= 0; i--) {
  person.push(arr[i]);
}

function snack(arr) {
  let stack = [];
  let cur = 1;
  let person = [...arr].reverse(); // 원본 배열을 뒤집음

  while (person.length > 0) {
    if (person[person.length - 1] === cur) {
      cur++;
      person.pop();
    } else if (stack.length > 0 && stack[stack.length - 1] === cur) {
      stack.pop();
      cur++;
    } else {
      stack.push(person.pop());
    }
  }
  if (person.length === 0) {
    return 'Nice';
  }
  return 'Sad';
}

console.log(snack(arr));
