#!/usr/bin/node
// A script that prints the title of a Star Wars movie where the episode number matches a given integer.

// Importing the request module
const request = require('request');

// Getting API URL from the command line argument
const apiUrl = process.argv[2];
const characterId = '18';

// Requesting data from Star wars API
request(apiUrl, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    let count = 0;
    // Parsing received body to the JSON object
    const films = JSON.parse(body).results;

    films.forEach((film) => {
      film.characters.forEach(
        (character) => character.includes(characterId) && count++
      );
    });

    console.log(count);
  }
});
