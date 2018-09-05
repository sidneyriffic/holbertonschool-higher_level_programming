#!/usr/bin/node

module.exports.converter = function (base) {
  let myConverter = function (number) {
    return number.toString(base);
  };
  return myConverter;
};
