let fs = require('fs');
let input = fs.readFileSync('io.txt').toString().trim();

a = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z='];

let replaceAlpha = a.reduce((acc, cur) => {
  return acc.replaceAll(cur, '*');
}, input);

console.log(replaceAlpha.length);
