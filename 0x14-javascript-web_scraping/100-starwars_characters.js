#!/usr/bin/node

const request = require('request');

request('http://swapi.co/api/films/' + process.argv[2], function (err, res, body) {
  if (err) console.log(err);
  else {
    let characters = JSON.parse(body).characters;
    for (let character in characters) {
      request(characters[character], function (err, res, body) {
        if (err) console.log(err);
        else {
          console.log(JSON.parse(body).name);
        }
      });
    }
  }
});
