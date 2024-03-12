#!/usr/bin/bnode

class Rectangle {
  constructor (w, h) {
    if (!(isNaN(w) || w < 1 || isNaN(h) || h < 1)) {
      this.width = w;
      this.height = h;
    }
  }
}

module.exports = Rectangle;
