function combi(arr, n) {
  const result = [];

  function backtrack(temp) {
    if (temp.length === n) {
      result.push([...temp]);
      return;
    }
    for (let i = 0; i < arr.length; i++) {
      temp.push(arr[i]);
      backtrack(temp);
      temp.pop();
    }
  }

  backtrack([]);

  return result;
}

let arr = [1, 2, 3];

console.log(combi(arr, 2));

function permu(arr, n) {
  const result = [];
  const visited = Array(arr.length).fill(false);

  function backtrack(temp) {
    if (temp.length === n) {
      result.push([...temp]);
      return;
    }

    for (let i = 0; i < arr.length; i++) {
      if (visited[i]) continue;

      temp.push(arr[i]);
      visited[i] = true;
      backtrack(temp);
      visited[i] = false;
      temp.pop();
    }
  }

  backtrack([]);

  return result;
}

console.log(permu(arr, 2));
