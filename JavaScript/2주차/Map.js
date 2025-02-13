let window = new Map();

window.set(1, 1);
window.set(1, (window.get(1) || 0) + 1);
window.set(3, 1);

console.log(window);

console.log(window.set(window.get(1) || 1, window.get(1) + 1));
console.log(window.get(1));
