function func() {
  return 'func 이야';
}

const func2 = () => {
  return 'func2 에용';
};

let function4 = (a) => {
  return a;
};

function func3(a, b) {
  return a() + ' ' + b();
}

console.log(func3(func, func2));

console.log(typeof {});

console.log(typeof func2);

console.log(function4(func));

let a = [1, 2, 3, 4, 5];
a.forEach((a) => console.log(a));

const h = () => 'b';

const obj = { 1: '2' };

console.log(obj.length);

const STR = ['1', '2', '3'];

console.log(h());

console.log(typeof +STR[0]);

console.log(typeof STR[1]);

console.log(typeof []);
console.log(typeof STR);

let f = [1, 2, 3, 4, 5];

let b = f.forEach((a) => {
  return console.log(a);
});

let c = f.map((a) => a);

let d = f.map((a) => {
  return a + 10;
});

console.log(b);
console.log(c);
