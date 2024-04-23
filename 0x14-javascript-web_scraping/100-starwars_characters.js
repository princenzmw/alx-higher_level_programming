#!/usr/bin/node
// a script that prints all characters of a Star Wars movie
// ALX Starwars API: https://swapi-api.hbtn.io/api/films/:id
// from https://swapi-api.alx-tools.com/

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

request(url, async (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const characters = JSON.parse(body).characters;
    for (const character of characters) {
      const name = await new Promise((resolve, reject) => {
        request(character, (error, response, body) => {
          if (error) {
            reject(error);
          } else {
            resolve(JSON.parse(body).name);
          }
        });
      });
      console.log(name);
    }
  }
});
