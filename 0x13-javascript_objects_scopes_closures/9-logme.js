#!/usr/bin/node

module.exports.logMe = function (item) {
  console.log(`${module.exports.logMe.count}: ${item}`);
  module.exports.logMe.count++;
};

module.exports.logMe.count = 0;
