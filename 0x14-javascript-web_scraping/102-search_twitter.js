#!/usr/bin/node

const request = require('request');

const key = Buffer.from(process.argv[2] + ':' + process.argv[3]).toString('base64');

function callsearch (oauthkey) {
  let searchoptions = {
    'url': 'https://api.twitter.com/1.1/search/tweets.json',
    'headers': {
      'Authorization': 'Bearer ' + oauthkey,
      'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
    },
    'qs': {
      'q': process.argv[4],
      'count': 5
    }
  };

  request.get(searchoptions, function (err, res, body) {
    if (err) console.log('error', err);
    else {
      let results = JSON.parse(body);
      for (let result in results.statuses) {
        result = results.statuses[result];
        console.log(`[${result.id}] ${result.text} by ${result.user.name}`);
      }
    }
  });
}

let options = {
  'url': 'https://api.twitter.com/oauth2/token',
  'headers': {
    'Authorization': 'Basic ' + key,
    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
  },
  'body': 'grant_type=client_credentials'
};

request.post(options, function (err, res, body) {
  if (err) console.log(err);
  else {
    if (res.statusCode === 200) {
      callsearch(JSON.parse(body).access_token);
    }
  }
});
