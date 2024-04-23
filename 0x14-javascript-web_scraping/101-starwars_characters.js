#!/usr/bin/node
// Print the names of all characters in a given film in the same order of the list “characters” in the /films/ response

const request = require('request');
const filmId = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${filmId}`;

request(url, async function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const characters = JSON.parse(body).characters;
    for (const character of characters) {
      await new Promise((resolve, reject) => {
        request(character, function (error, response, body) {
          if (error) {
            reject(error);
          } else {
            console.log(JSON.parse(body).name);
            resolve();
          }
        });
      });
    }
  }
});
