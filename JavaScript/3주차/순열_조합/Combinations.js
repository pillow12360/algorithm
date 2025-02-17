function Combinations(arr, n) {
  const result = [];

  function backtrack(temp, start) {
    if (temp.length === n) {
      result.push([...temp]);
      return;
    }

    for (let i = start; i < arr.length; i++) {
      temp.push(arr[i]);
      backtrack(temp, i + 1);
      temp.pop();
    }
  }

  backtrack([], 0);
  return result;
}

let arr = [1, 2, 3];
let n = 2;

console.log(Combinations(arr, n));
