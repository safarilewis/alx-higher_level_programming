#!/usr/bin/node
const fs = require("fs");
const text = process.argv[3];
try {
  fs.writeFile(process.argv[2], text, "utf-8");
} catch (err) {
  console.error(err);
}
