#!/usr/bin/node
// script that displays the status code of a GET request

// import the request module
const request = require('request');

// Get the command line arguments
const url = process.argv[2];

// Make the request
request(url, function (error, response, body) {
  if (!error) {
    console.log('code:', response.statusCode);
  }
});
