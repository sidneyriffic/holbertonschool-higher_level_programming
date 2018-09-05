#!/usr/bin/node

let fs = require('fs');

let file1 = fs.readFileSync(process.argv[2], 'utf8');
let file2 = fs.readFileSync(process.argv[3], 'utf8');
fs.writeFileSync(process.argv[4], file1 + file2);
