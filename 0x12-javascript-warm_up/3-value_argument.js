#!/usr/bin/node

const { argv } = require('node:process');

let count = 0;
for (const i in argv) {
  if (Object.prototype.hasOwnProperty.call(argv, i)) {
    count++;
  }
}

if (count === 2) {
  console.log('No arguments');
}

if (count === 3) {
  console.log(argv[2]);
}
