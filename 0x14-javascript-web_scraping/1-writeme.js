#!/usr/bin/node
// A Node script that writes a string to a file.

// import the fs (file system) module
const fs = require('fs');

// Get the command line arguments
const filePath = process.argv[2];
const content = process.argv[3];

// Write the data to file
fs.writeFile(filePath, content, 'utf8', (err) => {
  if (err) {
    console.log(err);
  }
});
