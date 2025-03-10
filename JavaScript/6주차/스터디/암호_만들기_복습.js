function isVowel(ch) {
  return ['a', 'e', 'i', 'o', 'u'].includes(ch);
}

function backtrack(arr, l) {
  if ((arr.length === l) & is_valid(arr)) {
    answer.push(arr);
  }
}
