#!/usr/bin/node
const SquareP = require('./5-square');

class Square extends SquareP {
  charPrint (c) {
    const ch = typeof c === 'undefined' ? 'X' : c;
    console.log(this.toString(ch));
  }
}

module.exports = Square;
