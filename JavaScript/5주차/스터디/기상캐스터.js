let fs = require('fs');
let input = fs.readFileSync('io.txt', 'utf-8').split('\n');

let [h, w] = input[0].split(' ');

let map = input.slice(1).map((i) => i.split(''));

// console.log(h, w, map);

for (let i = 0; i < h; i++) {
  let cloud = -1;
  for (let j = 0; j < w; j++) {
    if (map[i][j] === 'c') {
      map[i][j] = 0;
      cloud = 0;
    } else if (cloud >= 0 && map[i][j] === '.') {
      cloud += 1;
      map[i][j] = cloud;
    } else if (cloud === -1 && map[i][j] === '.') {
      map[i][j] = -1;
    }
  }
}

console.log(map.map((i) => i.join(' ')).join('\n'));
