#!/usr/bin/node

const fs = require('fs');
const request = require('request');

request.get(process.argv[2], function (err, res, data) {
  if (err) console.log(err);
  else {
    fs.writeFile(process.argv[3], data, 'utf-8', (err, res) => {
      if (err) console.log(err);
    });
  }
});
