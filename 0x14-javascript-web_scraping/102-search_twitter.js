#!/usr/bin/node

const request = require('request');
//const base64 = require('base-64');
//const utf8 = require('utf8');

const key = Buffer.from(process.argv[2] + ':' + process.argv[3]).toString('base64');

//console.log(key);

let options = {
  'url': 'https://api.twitter.com/oauth2/token',
  'headers': {
/*    'User-Agent': 'My Twitter App v1.0.23',*/
    'Authorization': 'Basic ' + key,
    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
/*    'Content-Length': '29',
    'Accept-Encoding': 'gzip'*/
  },
  'body': 'grant_type=client_credentials'
}

//console.log(options);

function callsearch(oauthkey) {
  options = {
    'url': 'https://api.twitter.com/1.1/search/tweets.json',
    'headers': {
      'Authorization': 'Bearer ' + oauthkey,
      'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
    },
    'qs': {
      'q': process.argv[4],
      'count': 5
    }
  }
//  console.log(options);
  
  request.get(options, function (err, res, body) {
    if (err) console.log(err);
    else {
//      console.log("search code", res.statusCode);
      results = JSON.parse(body);
//      console.log(results);
      for (let res in results.statuses) {
	res = results.statuses[res];
//	console.log("the rest", res)
	console.log(`[${res.id}] ${res.text} by ${res.user.name}`)
      }
    }
  });
}


request.post(options, function (err, res, body) {
  if (err) console.log(err);
  else {
/*    console.log("oauth code", res.statusCode);
    console.log(body);*/
    if (res.statusCode == "200") {
      callsearch(JSON.parse(body).access_token);
    }
  }
});
