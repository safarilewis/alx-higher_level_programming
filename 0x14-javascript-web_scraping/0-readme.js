#!/usr/bin/node
const file = process.argv[2];
let reader = new FileReader();
reader.readAsText(file, "utf-8");
reader.onload = function () {
  console.log(reader.result);
};
reader.onerror = function () {
  console.log(reader.error);
};
