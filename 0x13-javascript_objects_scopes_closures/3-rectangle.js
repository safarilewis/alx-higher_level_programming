#!/usr/bin/node
module.exports = class Rectangle {
    constructor (w, h) {
      if (w && h && w > 0 && h > 0) {
        this.width = w;
        this.height = h;
      }
    }
  
    print () {
      console.log(('X'.repeat(this.width) + '\n').repeat(this.height - 1) + 'X'.repeat(this.width));
    }
};
