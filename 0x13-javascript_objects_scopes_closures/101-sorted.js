#!/usr/bin/node

let dict = require('./101-data').dict;

let newdict = {};
for (let uid in dict) {
  if (newdict[dict[uid]] === undefined) {
    newdict[dict[uid]] = [];
  }
  newdict[dict[uid]].push(uid);
}

console.log(newdict);
