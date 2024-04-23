#!/usr/bin/node
// A script that prints the title of a Star Wars movie where the episode number matches a given integer.

const request = require('request');

const episode = process.argv[2];
const movie = `https://swapi-api.alx-tools.com/api/films/${episode}`;

request(movie, (error, response) => {
  if (error) {
    console.log('Error: ', error);
  } else {
    const obj = JSON.parse(response.body);
    console.log(obj.title);
  }
});
