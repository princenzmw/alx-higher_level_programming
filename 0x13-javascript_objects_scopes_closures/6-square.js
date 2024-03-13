#!/usr/bin/node
const SquareBase = require('./5-square');

class Square extends SquareBase {
  // Constructor is removed because it's redundant

  charPrint (c) {
    if (!c) {
      c = 'X';
    }
    for (let i = 0; i < this.width; i++) {
      let row = '';
      for (let j = 0; j < this.width; j++) {
        row += c;
      }
      console.log(row);
    }
  }
}

module.exports = Square;
