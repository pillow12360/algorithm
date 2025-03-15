let fs = require('fs');
let input = fs.readFileSync('io.txt').toString().split('\n');

let n = +input[0];
let ball = input[1].split('');

let red = 0;
let blue = 0;

if (ball.at(-1) === 'R') {
  while (ball.at(-1) === 'R') {
    ball.pop();
  }

  for (let i = 0; i < ball.length; i++) {
    if (ball[i] === 'R') red++;
    else blue++;
  }
  console.log(Math.min(red, blue));
  process.exit();
} else {
  while (ball.at(-1) === 'B') {
    ball.pop();
  }
  for (let i = 0; i < ball.length; i++) {
    if (ball[i] === 'R') red++;
    else blue++;
  }
  console.log(Math.min(red, blue));
  process.exit();
}
