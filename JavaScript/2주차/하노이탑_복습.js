let num = 3;

function hanoi(n, from, target, temp) {
  if (n === 1) {
    console.log(`${from} -> ${target}`);
  }
  hanoi(n - 1, from, temp, target);

  console.log(`${from} -> ${target}`);
  hanoi(n - 1, temp, target, from);
}

hanoi(num, 'A', 'C', 'B');
