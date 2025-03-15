function sol(balls) {
  let answer = Infinity;

  // 빨간공을 움직일 경우.
  let check = false;
  let cnt = 0;
  for (let i = balls.length - 1; i >= 0; i--) {
    if (balls[i] === 'B') {
      check = true;
    }
    if (check && balls[i] === 'R') {
      cnt++;
    }
  }
  if (cnt < answer) answer = cnt;
  check = false;
  cnt = 0;
  for (let i = 0; i < balls.length; i++) {
    if (balls[i] === 'B') {
      check = true;
    }
    if (check && balls[i] === 'R') {
      cnt++;
    }
  }
  if (cnt < answer) answer = cnt;

  // 파란공을 움직일 경우.
  check = false;
  cnt = 0;
  for (let i = balls.length - 1; i >= 0; i--) {
    if (balls[i] === 'R') {
      check = true;
    }
    if (check && balls[i] === 'B') {
      cnt++;
    }
  }
  if (cnt < answer) answer = cnt;
  check = false;
  cnt = 0;
  for (let i = 0; i < balls.length; i++) {
    if (balls[i] === 'R') {
      check = true;
    }
    if (check && balls[i] === 'B') {
      cnt++;
    }
  }
  if (cnt < answer) answer = cnt;

  return answer;
}
function main() {
  const input = require('fs')
    .readFileSync('io.txt')
    .toString()
    .trim()
    .split('\n');
  let balls = input[1].split('');
  console.log(sol(balls));
}
main();
