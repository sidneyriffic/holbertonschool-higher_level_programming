#!/usr/bin/node

module.exports.esrever = function (list) {
  let newlist = [];
  let c = 0;
  for (let l = list.length - 1; l >= 0; l--, c++) {
    newlist[c] = list[l];
  }
  return newlist;
};
