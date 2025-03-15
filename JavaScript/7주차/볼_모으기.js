let fs = require('fs');
let input = fs.readFileSync('io.txt').toString().split('\n');

let n = +input[0];
let ball = input[1].split('');

ball = ball.reverse();

let red = 0;
let blue = 0;

// red
let red_start = 0;
let blue_start = 0;

for (let i = 0; i < ball.length; i++) {
  if (ball[i] === 'B') {
    red_start = i;
    break;
  }
}

for (let i = red_start; i < ball.length; i++) {
  if (ball[i] === 'R') {
    red++;
  }
}

// blue

for (let i = 0; i < ball.length; i++) {
  if (ball[i] === 'R') {
    blue_start = i;
    break;
  }
}

for (let i = blue_start; i < ball.length; i++) {
  if (ball[i] === 'B') {
    blue++;
  }
}

console.log(Math.min(red, blue));
