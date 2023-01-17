#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (err, response, body){
    if (err){
        console.error(err);
    }
    const todos = JSON.parse(body);
    const answer = {};
    for (const todo of todos){
        if (todo.completed){
            if(!answer[todo.userId]){
                answer[todo.userId] = 1;
            }
            answer[todo.userId]++;
        }
    }
    console.log(answer);
});