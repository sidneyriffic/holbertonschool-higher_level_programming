#!/usr/bin/node

let fs = require('fs');

try {
  let file1 = fs.readFileSync(process.argv[2], 'utf8');
  console.log(file1);
} catch (err) {
  console.log(err);
}
