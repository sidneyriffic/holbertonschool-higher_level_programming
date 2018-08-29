#!/usr/bin/node

switch (process.argv.length) {
  case 2:
    console.log('No arguments');
    break;
  case 3:
    console.log('Argument found');
    break;
  default:
    console.log('Arguments found');
}
