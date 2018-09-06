#!/usr/bin/node

const request = require('request');

request(process.argv[2], function (err, res, body) {
  if (err) console.log(err);
  else {
    let completetasks = {};
    let todos = JSON.parse(body);
    for (let task in todos) {
      if (todos[task].completed === true) {
        if (completetasks[todos[task].userId]) completetasks[todos[task].userId]++;
        else completetasks[todos[task].userId] = 1;
      }
    }
    console.log(completetasks);
  }
});
