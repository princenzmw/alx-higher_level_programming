#!/usr/bin/node

const { argv } = require('node:process');

if (argv.length < 3) {
  console.log('Not a number');
} else {
  parseInt(argv[2]) ? console.log(`My number: ${parseInt(argv[2])}`) : console.log('Not a number');
}
