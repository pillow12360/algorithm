const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');
const [n, m] = input[0].split(' ').map((el) => +el);
let map = input.slice(1, n + 1).map((el) => el.split(''));
let queue = [];
queue.push([0, 0, 1]);
while (queue.length > 0) {
  let [a, b, len] = queue.shift();
  if (a === n - 1 && b === m - 1) {
    console.log(len);
    break;
  } else {
    map[a][b] = '0';
    if (a < n - 1 && map[a + 1][b] === '1') queue.unshift([a + 1, b, len + 1]);
    if (b < m - 1 && map[a][b + 1] === '1') queue.unshift([a, b + 1, len + 1]);
    if (a > 0 && map[a - 1][b] === '1') queue.push([a - 1, b, len + 1]);
    if (b > 0 && map[a][b - 1] === '1') queue.push([a, b - 1, len + 1]);
  }
}
