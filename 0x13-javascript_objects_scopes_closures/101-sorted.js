#!/usr/bin/node

// Import the dictionary from 101-data.js file
const data = require('./101-data').dict;

// Create a new empty dictionary to store occurrences as keys and user ids as values
const occurrencesById = {};

// Loop through each user id in the imported dictionary
for (const userId in data) {
  // Get the number of occurrences for this user id
  const occurrence = data[userId];

  // If this is the first time we see this number of occurrences,
  // create a new array to hold user ids
  if (!occurrencesById[occurrence]) {
    occurrencesById[occurrence] = [];
  }

  // Add the current user id to the array for this number of occurrences
  occurrencesById[occurrence].push(userId);
}

// Print the new dictionary
console.log(occurrencesById);
