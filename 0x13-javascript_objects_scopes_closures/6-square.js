#!/usr/bin/node
const Squar = require('./5-square');

class Square extends Squar {
  constructor (size) {
    super(size);
    this.size = size;
  }

  charPrint (c) {
    if (!c) {
      for (let i = 0; i < this.size; i++) {
        let row = '';
        for (let j = 0; j < this.size; j++) {
          row += 'X';
        }
        console.log(row);
      }
    } else {
      for (let i = 0; i < this.size; i++) {
        let row = '';
        for (let j = 0; j < this.size; j++) {
          row += c;
        }
        console.log(row);
      }
    }
  }
}

module.exports = Square;
