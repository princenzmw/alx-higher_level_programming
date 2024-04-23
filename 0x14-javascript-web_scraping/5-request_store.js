#!/usr/bin/node
// A script that gets the contents of a webpage and stores it in a file.

const request = require('request');
const fs = require('fs');
const urlApi = process.argv[2];
const outputFile = process.argv[3];

request(urlApi, (error, response) => {
  if (error) {
    console.log('Error: ', error);
  } else if (response) {
    const content = response.body;
    fs.writeFile(outputFile, content, 'utf-8', error => {
      if (error) console.log('Error: ', error);
    });
  } else {
    console.log('Unable to complete the request');
  }
});
