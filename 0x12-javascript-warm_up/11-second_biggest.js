#!/usr/bin/node

const { argv } = require('node:process');

const myArgs = argv.slice(2);
const myArray = [];

myArgs.forEach(a => {
  myArray.push(parseInt(a));
});

const sorted = myArray.sort((a, b) => b - a);

if (myArgs.length <= 1) {
  console.log(0);
} else {
  console.log(sorted[1]);
}
