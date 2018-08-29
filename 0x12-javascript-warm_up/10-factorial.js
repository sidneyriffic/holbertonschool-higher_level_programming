#!/usr/bin/node

let factorial = parseInt(process.argv[2]);

if (!factorial) {
  console.log('1');
} else {
  let total = 1;
  while (factorial > 1) {
    total = total * factorial--;
  }
  console.log(total);
}
