#!/usr/bin/node
// A script that computes the number of tasks completed by user id.
// the used API is https://jsonplaceholder.typicode.com/todos

const request = require('request');
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const tasks = JSON.parse(body);
    const completed = {};
    for (const task of tasks) {
      if (task.completed === true) {
        if (completed[task.userId] === undefined) {
          completed[task.userId] = 1;
        } else {
          completed[task.userId]++;
        }
      }
    }
    console.log(completed);
  }
});
