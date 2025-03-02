let fs = require('fs');
let input = fs.readFileSync('io.txt').toString().trim().split('');

if (input.length <= 1) {
  console.log('NO');
  process.exit();
}

while (input.length) {
  let a = input.pop();

  if (a === 'i') {
    if (input.pop() === 'p') {
      continue;
    } else {
      console.log('NO');
      process.exit();
    }
  } else if (a === 'a') {
    {
      if (input.pop() === 'k') {
        continue;
      } else {
        console.log('NO');
        process.exit();
      }
    }
  } else if (a === 'u') {
    {
      if (input.pop() === 'h') {
        if (input.pop() === 'c') {
          continue;
        } else {
          console.log('NO');
          process.exit();
        }
      } else {
        console.log('NO');
        process.exit();
      }
    }
  } else {
    console.log('NO');
    process.exit();
  }
}

console.log('YES');
