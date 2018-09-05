#!/usr/bin/node

module.exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  for (let ele in list) {
    if (list[ele] === searchElement) {
      count++;
    }
  }
  return count;
};
