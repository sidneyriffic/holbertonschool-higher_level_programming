#!/usr/bin/node

const request = require('request');

request('http://swapi.co/api/films/' + process.argv[2], async function (err, res, body) {
  if (err) console.log(err);
  else {
    let characters = JSON.parse(body).characters;
    const listpromise = new Promise(async resolve => {
      let charnames = [];
      for (let character in characters) {
        let charname = '';
        const namepromise = new Promise(resolve => {
          request(characters[character], function (err, res, body) {
            if (err) console.log(err);
            else {
              console.log(JSON.parse(body).name);
            }
            resolve(charname);
          });
        });
        await namepromise;
      }
      resolve(charnames);
    });
    await listpromise;
  }
});
