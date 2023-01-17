#!/usr/bin/node
const file = arguments[0];
let reader = new FileReader();
reader.readAsText(file, "utf-8");
reader.onload = function () {
  console.log(reader.result);
};
reader.onerror = function () {
  console.log(reader.error);
};
