#!/usr/bin/node
// A Node script that writes a string to a file.

const fs = require('fs');
const filePath = process.argv[2];
const content = process.argv[3];

fs.writeFile(filePath, content, 'utf8', (err) => {
  if (err) {
    console.log(err);
  } else {
    console.log(content);
  }
});
