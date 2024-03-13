#!/usr/bin/node
const fs = require('fs');

// Get file paths from the arguments passed to the script
const fileAPath = process.argv[2];
const fileBPath = process.argv[3];
const fileCPath = process.argv[4];

// Read the content of the first file
const contentA = fs.readFileSync(fileAPath, { encoding: 'utf8', flag: 'r' });

// Read the content of the second file
const contentB = fs.readFileSync(fileBPath, { encoding: 'utf8', flag: 'r' });

// Concatenate the contents of both files
const combinedContent = contentA + contentB;

// Write the concatenated content to the destination file
fs.writeFileSync(fileCPath, combinedContent);
