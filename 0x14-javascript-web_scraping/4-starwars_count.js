#!/usr/bin/node
const request = require('request');
const wedge = "https://swapi-api.alx-tools.com/api/people/18/";
request (process.argv[2], function (err, response, body){
    if (err){
        console.error(err);
    }
    const films = JSON.parse(body);
    const characters = films['characters'];
    let count = 0;
    let answer;
    for (count = 0; count < characters.length; count++){
        if (characters[count] == wedge){
            answer = answer + 1;
        }
    }
    console.log(answer);
} )