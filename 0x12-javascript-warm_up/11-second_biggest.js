#!/usr/bin/node

let second = parseInt(process.argv[3]);

if (isNaN(second)) {
  console.log('0');
  process.exit();
}

let first = parseInt(process.argv[2]);

if (first < second) {
  let temp = first;
  first = second;
  second = temp;
}

for (let i = 4; i < process.argv.length; i++) {
  let next = parseInt(process.argv[i]);
  if (next > second) {
    if (next > first) {
      second = first;
      first = next;
    } else {
      second = next;
    }
  }
}
console.log(second);
