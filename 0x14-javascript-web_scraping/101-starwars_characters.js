#!/usr/bin/node

const request = require('request');

request('http://swapi.co/api/films/' + process.argv[2], function (err, res, body) {
  if (err) console.log(err);
  else {
    let characters = JSON.parse(body).characters;
    let promiselist = [];
    for (let character in characters) {
      const namepromise = new Promise(resolve => {
        request(characters[character], function (err, res, body) {
          if (err) console.log(err);
          else {
            resolve(JSON.parse(body).name);
          }
        });
      });
      promiselist.push(namepromise);
    }
    Promise.all(promiselist).then(function (namelist) {
      for (let name in namelist) {
        console.log(namelist[name]);
      }
    });
  }
});
