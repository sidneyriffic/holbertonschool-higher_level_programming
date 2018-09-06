#!/usr/bin/node

let fs = require('fs');

fs.readFile(process.argv[2], 'utf8', (err, data) => {
  if (err) console.log(err);
  else console.log(data);
});
