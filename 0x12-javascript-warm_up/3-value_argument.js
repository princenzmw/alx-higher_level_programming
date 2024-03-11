#!/usr/bin/node

// Check if process.argv[2] is undefined, which would mean no arguments were passed.
if (process.argv[2] === undefined) {
  console.log('No argument');
} else {
  console.log(process.argv[2]);
}
